{
  'includes': [
    'wd.gypi',
  ],

  'variables': {
    'WD_BUILD_MONGOOSE%': '0',
    'MONGOOSE_INC_PATH%': 'src/third_party/mongoose',
  },

  'targets': [
    {
      'target_name': 'WebDriver_core',
      'type': 'static_library',
      'standalone_static_library': 1,
      'msvs_configuration_attributes': {
        'CharacterSet': '1'
      },

      'cflags': [
        '-fPIC',
        '-Wall',
        '-W',
        '-Wno-unused-parameter',
      ],

      'include_dirs': [
        'inc/',
        'src/',
        '<(MONGOOSE_INC_PATH)',
      ],

      'sources': [
        'src/webdriver/commands/alert_commands.cc',
        'src/webdriver/commands/appcache_status_command.cc',
#        'src/webdriver/commands/browser_connection_commands.cc',
        'src/webdriver/commands/command.cc',
        'src/webdriver/commands/cookie_commands.cc',
        'src/webdriver/commands/create_session.cc',
        'src/webdriver/commands/execute_async_script_command.cc',
        'src/webdriver/commands/execute_command.cc',
        'src/webdriver/commands/find_element_commands.cc',
        'src/webdriver/commands/html5_location_commands.cc',
        'src/webdriver/commands/html5_storage_commands.cc',
        'src/webdriver/commands/keys_command.cc',
        'src/webdriver/commands/log_command.cc',
        'src/webdriver/commands/mouse_commands.cc',
        'src/webdriver/commands/navigate_commands.cc',
        'src/webdriver/commands/response.cc',
        'src/webdriver/commands/screenshot_command.cc',
        'src/webdriver/commands/sessions.cc',
        'src/webdriver/commands/session_with_id.cc',
        'src/webdriver/commands/set_timeout_commands.cc',
        'src/webdriver/commands/source_command.cc',
        'src/webdriver/commands/target_locator_commands.cc',
        'src/webdriver/commands/title_command.cc',
        'src/webdriver/commands/url_command.cc',
        'src/webdriver/commands/webdriver_command.cc',
        'src/webdriver/commands/element_commands.cc',
        'src/webdriver/commands/window_commands.cc',
        'src/webdriver/commands/non_session_commands.cc',
        'src/webdriver/commands/xdrpc_command.cc',
        'src/webdriver/webdriver_route_patterns.cc',
        'src/webdriver/frame_path.cc',
        'src/webdriver/http_response.cc',
        'src/webdriver/value_conversion_traits.cc',
        'src/webdriver/webdriver_basic_types.cc',
        'src/webdriver/webdriver_capabilities_parser.cc',
        'src/webdriver/webdriver_element_id.cc',
        'src/webdriver/webdriver_view_id.cc',
        'src/webdriver/webdriver_error.cc',
        'src/webdriver/webdriver_logging.cc',
        'src/webdriver/webdriver_server.cc',
        'src/webdriver/webdriver_route_table.cc',
        'src/webdriver/webdriver_view_enumerator.cc',
        'src/webdriver/webdriver_view_factory.cc',
        'src/webdriver/webdriver_view_executor.cc',
        'src/webdriver/webdriver_session.cc',
        'src/webdriver/webdriver_session_manager.cc',
        'src/webdriver/webdriver_switches.cc',
        'src/webdriver/webdriver_util.cc',
        'src/webdriver/webdriver_view_runner.cc',
        'src/webdriver/webdriver_view_transitions.cc',
        'src/webdriver/url_command_wrapper.cc',
        'src/webdriver/versioninfo.cc',
        'src/webdriver/webdriver_version.cc',
      ],

      'conditions': [

        [ '<(WD_BUILD_MONGOOSE) == 1', {
          'sources': [
            'src/third_party/mongoose/mongoose.c',
          ],
        } ],

        [ 'mode == "debug"', {
          'cflags': [
            '-O0',
            '-g',
          ],
        } ],

        [ 'mode == "release"', {
          'cflags': [
            '-O3',
          ],

          'defines': [
            'NDEBUG',
          ],
        } ],

        [ 'mode == "release_dbg"', {
          'cflags': [
            '-O3',
            '-g',
          ],
        } ],
       
        ['OS=="linux"', {
          'defines': [
            '__STDC_FORMAT_MACROS',
            'OS_POSIX',
          ],
        } ],

        [ 'OS == "win"', {
          'defines': [
            '_WIN32',
            'OS_WIN',
            'NOMINMAX',
            '_CRT_RAND_S',
            'WIN32',
            '_WINSOCKAPI_',
          ],
          'msvs_configuration_attributes': {
            'CharacterSet': '1'
          },
        } ],
      ],
    }
  ],
}