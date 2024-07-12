from . import __version__ as app_version

app_name = "erpnext_chinese"
app_title = "ERPNext Chinese"
app_publisher = "yuzelin"
app_description = "ERPNext中文汉化，简化，优化"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "yuxinyong@163.com"
app_license = "MIT"

# Includes in <head>
# 由以下白名单方法覆盖实现，以解决延时翻译，手机不执行js代码问题
# app_include_js = ["erpnext_chinese.bundle.js"]

override_whitelisted_methods = {
    "frappe.desk.desktop.get_workspace_sidebar_items": "erpnext_chinese.overrides.custom_get_workspace_sidebar_items"
}