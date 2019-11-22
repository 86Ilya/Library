from django.utils.module_loading import import_string

from Library.settings import BALANCER_STRATEGY, DATABASES


class LibraryRouter:
    """
    Router for database queries
    """

    databases = DATABASES.copy()
    balancer = import_string(BALANCER_STRATEGY)(databases)

    def db_for_read(self, model, **hints):
        """
        Balance queries between instances
        """
        instance = self.balancer.balance(model)
        return instance

    def db_for_write(self, model, **hints):
        """
        Writes always go to default.
        """
        return self.databases['default']

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the default/replica pool.
        """
        db_list = list(self.databases)
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True

        # we don't need auth router in this project, so auth relations will be processing here
        if obj1._meta.app_label == 'auth' or obj2._meta.app_label == 'auth':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        return True
