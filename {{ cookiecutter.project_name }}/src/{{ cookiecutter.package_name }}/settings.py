"""Project settings. There is no need to edit this file unless you want to
change values from the Kedro defaults. For further information, including
these default values, see:
https://kedro.readthedocs.io/en/stable/kedro_project_setup/settings.html."""
# Add globals to template dict
from typing import Any, Dict, List, Optional

from kedro.config import TemplatedConfigLoader

# Instantiated project hooks.
# from imlp_data_processing.hooks import ProjectHooks

# HOOKS = (ProjectHooks(),)

# Installed plugins for which to disable hook auto-registration.
# DISABLE_HOOKS_FOR_PLUGINS = ("kedro-viz",)

# Class that manages storing KedroSession data.
# from kedro.framework.session.shelvestore import ShelveStore
# SESSION_STORE_CLASS = ShelveStore
# Keyword arguments to pass to the `SESSION_STORE_CLASS` constructor.
# SESSION_STORE_ARGS = {
#     "path": "./sessions"
# }

# Class that manages Kedro's library components.
# from kedro.framework.context import KedroContext
# CONTEXT_CLASS = KedroContext

# Directory that holds configuration.
# CONF_SOURCE = "conf"

# Class that manages how configuration is loaded.
# CONFIG_LOADER_CLASS = ConfigLoader
# Keyword arguments to pass to the `CONFIG_LOADER_CLASS` constructor.
# CONFIG_LOADER_ARGS = {
#       "config_patterns": {
#           "spark" : ["spark*/"],
#           "parameters": ["parameters*", "parameters*/**", "**/parameters*"],
#       }
# }

# Class that manages the Data Catalog.
# from kedro.io import DataCatalog
# DATA_CATALOG_CLASS = DataCatalog


class HookedConfigLoader(TemplatedConfigLoader):
    """Overrides configuration mapping of the TemplatedConfigLoader. The config is
    overridden in order to ensure that user_name, branch and bucket_name are mingled
    into a proper path on S3 that the user has access to.
    """

    def __init__(
        self,
        conf_source: str,
        env: str = None,
        runtime_params: Dict[str, Any] = None,
        config_patterns: Dict[str, List[str]] = None,
        *,
        base_env: str = "base",
        default_run_env: str = "local",
        globals_pattern: Optional[str] = None,
        globals_dict: Optional[Dict[str, Any]] = None,
        user_name_key: str = "user_name",
        branch_key: str = "branch",
        bucket_name_key: str = "bucket_name",
        folder_names_key: str = "folders"
    ):
        super().__init__(
            conf_source,
            env,
            runtime_params,
            config_patterns,
            base_env=base_env,
            default_run_env=default_run_env,
            globals_pattern=globals_pattern,
            globals_dict=globals_dict,
        )
        _altered_config_mapping = {
            "raw": "/".join(
                [
                    "s3:/",
                    self._config_mapping[bucket_name_key],
                    "01_raw",
                ]
            )
            + "/"
        }

        for folder_alias, full_folder_name in self._config_mapping[
            folder_names_key
        ].items():
            _altered_config_mapping[folder_alias] = (
                "/".join(
                    [
                        "s3:/",
                        self._config_mapping[bucket_name_key],
                        self._config_mapping[user_name_key],
                        self._config_mapping[branch_key],
                        full_folder_name,
                    ]
                )
                + "/"
            )
        self._config_mapping[folder_names_key] = _altered_config_mapping


CONFIG_LOADER_CLASS = HookedConfigLoader
CONFIG_LOADER_ARGS = {
    "globals_pattern": "*globals.yml",
}
