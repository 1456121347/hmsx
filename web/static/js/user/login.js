;
var user_login_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        $(".login_wrap .do-login").click(function(){
            var btn_target = $(this)
            if (btn_target.hasClass("disabled")) {
                alert("请不要重复提交")
                return;
            }
            var login_name = $(".login_wrap input[name=login_name]").val()
            var login_pwd = $(".login_wrap input[name=login_pwd]").val()
            console.log(login_name)
            console.log(login_pwd)

            // 前端校检 不为空 长度不小于1
            if (login_name == undefined || login_name.length < 1){
                alert('请输入正确的用户名')
                return;
            }
            if (login_pwd == undefined || login_pwd.length < 1){
                alert('请输入正确的密码')
                return;
            }
            btn_target.addClass("disabled")

            // Ajax 前后端分离的，数据格式json {key:value},前端发送数据是json格式，所以后端返回的也是json格式
            
            
            $.ajax({
                // url:common_ops.buildUrl("/user/login"),
                url:"login",
                type:"POST",
                data:{'login_name':login_name,'login_pwd':login_pwd},
                dataType:'json',
                success:function(resp){
                    btn_target.removeClass("disabled")
                    console.log(resp)
                    alert(resp.msg)
                }
            })
        })
    }
}


$(document).ready(function(){
    user_login_ops.init();
})