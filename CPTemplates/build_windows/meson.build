project('build_windows', 'c',
  default_options : ['warning_level=3'])

cc = meson.get_compiler('c')

shared_library('local.pyd',
           'local.c',
            include_directories: ['D:\\Tools\\Scoop\\apps\\python311\\current\\include'],
            dependencies: [cc.find_library('python311', dirs: 'D:\\Tools\\Scoop\\apps\\python311\\current\\libs')]
           )
