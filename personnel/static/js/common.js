function trim (str) {
    return str.replace(/^\s\s*/, '').replace(/\s\s*$/, '');
}

$(function(){
    var info = $("#person-info");
    var name = info.data('name');
    var info_txt = trim(info.html());

    info.editable(function(value, settings) {
        var value = trim(value);
        var csrf = $("[name=csrfmiddlewaretoken]").val();
        
        var params = {
            csrfmiddlewaretoken: csrf,
            info: value
        };

        $.post("/people/" + name + "/update_info", params);
        return value;
    }, {
        type: 'textarea',
        onblur: 'ignore',
        submit: 'Done',
        data: info_txt
    });
});
