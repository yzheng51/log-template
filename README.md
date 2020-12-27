# Log Template

log template project, below example shows the format

```log
2020-12-27 20:14:41,499 DEBUG    module[line:30] - this is main
2020-12-27 20:14:41,499 INFO     module[line:31] - this is main
2020-12-27 20:14:41,499 WARNING  module[line:32] - this is main
2020-12-27 20:14:41,499 ERROR    module[line:33] - this is main
2020-12-27 20:14:41,500 CRITICAL module[line:34] - this is main
2020-12-27 20:14:41,500 INFO     module[line:36] - creating an instance of module.utils.TestModuleA
2020-12-27 20:14:41,500 INFO     module.utils.TestModuleA[line:10] - creating an instance of TestModuleA
2020-12-27 20:14:41,500 INFO     module.utils.TestModuleA[line:13] - doing something
2020-12-27 20:14:41,500 INFO     module.utils.TestModuleA[line:15] - done doing something
2020-12-27 20:14:41,500 DEBUG    module.utils[line:20] - this is module.utils
2020-12-27 20:14:41,500 INFO     module.utils[line:21] - this is module.utils
2020-12-27 20:14:41,500 WARNING  module.utils[line:22] - this is module.utils
2020-12-27 20:14:41,500 ERROR    module.utils[line:23] - this is module.utils
2020-12-27 20:14:41,500 CRITICAL module.utils[line:24] - this is module.utils
2020-12-27 20:14:41,500 INFO     module.submodule.core.TestModuleB[line:10] - creating an instance of TestModuleB
2020-12-27 20:14:41,500 INFO     module.submodule.core.TestModuleB[line:13] - doing something
2020-12-27 20:14:41,500 INFO     module.submodule.core.TestModuleB[line:15] - done doing something
2020-12-27 20:14:41,500 DEBUG    module.submodule.core[line:20] - this is module.submodule.core
2020-12-27 20:14:41,500 INFO     module.submodule.core[line:21] - this is module.submodule.core
2020-12-27 20:14:41,500 WARNING  module.submodule.core[line:22] - this is module.submodule.core
2020-12-27 20:14:41,501 ERROR    module.submodule.core[line:23] - this is module.submodule.core
2020-12-27 20:14:41,501 CRITICAL module.submodule.core[line:24] - this is module.submodule.core
```
