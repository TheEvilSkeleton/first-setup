project('io.github.vanilla-os.FirstSetup',
          version: '0.1.9',
    meson_version: '>= 0.59.0',
  default_options: [ 'warning_level=2',
                     'werror=false',
                   ],
)

i18n = import('i18n')

gnome = import('gnome')

subdir('data')
subdir('vanilla_first_setup')
subdir('po')

gnome.post_install(
  glib_compile_schemas: true,
  gtk_update_icon_cache: true,
  update_desktop_database: true,
)