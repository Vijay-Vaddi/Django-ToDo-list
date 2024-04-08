$(document).ready(function () {
    $(document).on('click', '.incomplete-task', function () {
        var data_task_id = $(this).attr('data-task-id');

        var a = "{%";
        var b = "url";
        var c = "'task-update'";
        var d = "%}";
        var update_url = a+b+c  + data_task_id +d;
        $('#confirm-task-done').attr('action', update_url);

    });
});
