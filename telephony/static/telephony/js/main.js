/**
 * Created by bogdan on 11.10.16.
 */
        $(document).ready(function () {
            setInterval(function () {
                $.ajax({
                    url: "/telephony/check_new_call/" + len_calls,
                    type: "GET",
                    success: function (data) {
                        if (data == "1") {
                            location.reload()
                        }
                    }
                });
            }, 2500);
            $('#clear_all').click(function () {
                $.ajax({
                    url: "/telephony/clear_all/",
                    type: "GET",
                    success: function (data) {
                        if (data == "1") {
                            location.reload()
                        }
                    }
                });
            })
        });
        function check(id) {
            $('#' + id).fadeOut(1000);
            $('#none' + id).fadeIn(1000);
            $.ajax({
                url: "/telephony/change_call/" + id,
                type: "GET"
            });
        }
