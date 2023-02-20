# manifest_version

## 版本号，由google指定为2 支持将在2023年移除。

```
"manifest_version":2
"manifest_version":3
```

# name

## 插件名称

```
"name": "helloWorld"
```

# description

## 插件描述

```
"description":"hello world 插件"
```

# version

## 插件版本

```
"version":"1.0"
```

# icons

## 插件图标

```
"icons":{
    "128":"img/axolotl.png",
    "48":"img/axolotl.png",
    "16":"img/axolotl.png"
}
```

# action

```

"action": {
    "default_icon": "img/axolotl.png",
    "default_popup": "popup.html"
  }
  
插件图标
default_icon
"default_icon":"img/axolotl.png"

点击图标后弹出的html互动文件
default_popup
 "default_popup":"popup.html"
```

# background

## 在浏览器后台Service Workers中运行的程序

```
"background": {
    "service_worker": "js/background.js",
    "type": "module"
  },
```

# permissions

## 谷歌权限

```

"permissions": [
    "contextMenus"
]

"contextMenus",
存储权限
"storage",
"tabs",
"tts",
"notifications"
```

# content_scripts

## 插入到目标页面中执行的JS

```

"content_scripts": [
  {
    "matches": ["<all_urls>"],
    "js": ["js/jquery-3.6.0.min.js", "js/content.js"],
    "run_at": "document_start"
  }
],
```

# options_ui

## 选项页面 非必要

```
"options_ui": {
  "page": "html/options.html",
  "open_in_tab": true
}
```
