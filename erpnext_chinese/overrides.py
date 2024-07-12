import frappe
from frappe.desk.desktop import get_workspace_sidebar_items

@frappe.whitelist()
def custom_get_workspace_sidebar_items():
    data = get_workspace_sidebar_items()
    if frappe.local and frappe.local.lang and frappe.local.lang == 'zh':
        trans_map = [
            ['Reports &amp; Masters', '主数据、业务交易、报表'],
            ["Masters &amp; Reports",'主数据、业务交易、报表'],            
            ['Reports & Masters', '主数据、业务交易、报表'],
            ["Masters & Reports",'主数据、业务交易、报表'],
            ['Elements', '定制项'],
            ['Quick Access', '快捷方式'],
            ['Your Shortcuts', '快捷方式'],
            ['Shortcuts', '快捷方式'],
            ['Quick Links', '简易列表'],
            ['<b>Settings</b>', '<b>设置</b>'],
            ['Integrations', '应用集成'],  
            ['Get started','开始使用'],
            ['Components to build your app','应用构建组件'],          
            ['Documents', '单据']
        ]
        pages = data.get('pages', [])        
        for page in pages:
            content = page.content
            for (en, zh) in trans_map:
                if content:
                    content = content.replace(en,zh)
            page.content = content                                
    return data