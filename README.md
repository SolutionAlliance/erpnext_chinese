## ERPNext Chinese
ERPNext中文汉化
本应用只包括中文汉化文件translations/zh.csv 实现了绝大部分标准功能支持的界面汉化,另外一些代码级汉化在另一个开箱即

### 特别说明
- 1. 因翻译机制的原因，安装此汉化应用后，还会有个别页面的标签来自于未通过标准程序加载到待翻译文本中，导致即使翻译文件zh.csv中包括了对应的翻译词条，也不能翻译的问题（如主页左侧菜单的Modules,Domain等），可通过用户界面新增翻译词条解决这部分翻译问题

- 2. 还有很多标准控件上的自带标签，属于控件js范畴，因为此应用不涉及修改标准功能，所以相关自带控件部分标签也没有翻译。
 
本人在discuss.erpnext.com及github.com官网帐号是szufisher, 本人QQ: 2474916185, 微信：szufisher

### 使用方法

#### 先决条件

进入 bench 工作台目录；

> 1.新安装
>> 1.1、获取对应版本APP

```
bench get-app https://gitee.com/SolutionAlliance/erpnext_chinese.git
```

>> 1.2、安装APP(有多个站点且未设默认站点的请加--site参数）
```
bench install-app erpnext_chinese
```

升级（之前安装过未拆分前版本的请谨慎更新）
> 2.1、bench update 命令

```
bench update --apps erpnext_chinese --pull --reset
```

>> 2.2 重新编译JS等资源文件

bench build --app erpnext_chinese --force

>> 2.3 通过本应用中的插件机制向打印格式单据类型中新增两个字段(同步，新安装时不需要这一步，也可运行标准的bench migrate 命令，会对所有app作升级后同步数据库表处理)
```
bench console
In [6]: from frappe.utils.fixtures import sync_fixtures

In [7]: sync_fixtures('erpnext_chinese')
```

#### 卸载
> 3.1 从站点卸载 

```
bench uninstall-app erpnext_chinese
```

> 3.2 从整个bench环境卸载,移除整个应用目录

```
bench remove-app erpnext_chinese
```

欢迎提交问题和反馈建议。

### 特别感谢
- [yuzelin-erpnext_oob]( https://gitee.com/yuzelin/erpnext_oob)
- [yuzelin-erpnext_chinese](https://gitee.com/yuzelin/erpnext_chinese.git)

#### License
MIT