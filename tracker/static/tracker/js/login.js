/**
 * Created by bogdan on 11.10.16.
 */
$(document).ready(function () {
    $('.loginmodal-submit').click(function () {
        $.ajax({
            url: "/authorization/login/",
            type: "POST",
            data: $('.myfor').serialize(),

            success: function (data) {
                if (data == "1") {
                    location.reload()
                }
                else {
                    $('#info-log').fadeIn(2000);
                    setTimeout(function () {
                        $('#info-log').fadeOut(2000)
                    }, 7000)
                }
            }
        });
    })
});