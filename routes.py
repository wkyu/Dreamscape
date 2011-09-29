COMING_SOON = True
default_application = 'welcome'
default_controller = 'default'
default_function = 'index'

if COMING_SOON:
    default_function = 'coming_soon'

routers = dict(
    BASE = dict(default_application='welcome'),
)