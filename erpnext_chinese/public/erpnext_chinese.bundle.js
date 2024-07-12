$(document).on('page-change', function() {
    setTimeout(function(){
        if (frappe.boot.lang == 'zh' && frappe.get_route() && 
            (frappe.get_route().at(-1) == 'Workspaces' || frappe.get_route()[0] == 'Workspaces')){
            let trans_map = [['Reports &amp; Masters', '主数据、业务交易、报表'],
                ["Masters & Reports",'主数据、业务交易、报表'],
                ['Reports & Masters', '主数据、业务交易、报表'],
                ['Elements', '定制项'],
                ['Quick Access', '快捷方式'],
                ['Your Shortcuts', '快捷方式'],
                ['Settings', '设置'],
                ['Integrations', '应用集成'],
                ['My Workspaces', '我的工作区'],
                ['MY WORKSPACES', '我的工作区'],
                ['Documents', '单据']
            ];
            $.each(trans_map, function(i,v){
                $('div.ce-block__content span b:contains("'+v[0]+'")').html(v[1]);
            })
        }
    },
    500)    
});