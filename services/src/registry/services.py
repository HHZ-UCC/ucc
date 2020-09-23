from django.apps import apps
import logging

logger = logging.getLogger(__name__)

class RegistryService:
    registered_apps = {}
    
    def get_registered_apps(self):
        if self.registered_apps:
            return list(self.registered_apps.values())
        else:
            registry_method_name = 'get_registry_info'
            appconfigs = apps.get_app_configs()
            for config in appconfigs:
                is_registrable = hasattr(config, registry_method_name) and callable(getattr(config, registry_method_name))
                if is_registrable:
                    logger.info("Registering app %s", config.verbose_name)
                    registry_info = config.get_registry_info()
                    self.registered_apps[config.verbose_name] = registry_info
        return list(self.registered_apps.values())