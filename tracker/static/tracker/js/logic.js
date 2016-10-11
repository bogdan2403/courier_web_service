/**
 * Created by bogdan on 11.10.16.
 */
navigator.geolocation.getCurrentPosition(function (position) {
    start = {lat: position.coords.latitude, lng: position.coords.longitude};
});
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: end,
        scrollwheel: true,
        zoom: 7
    });
}
function directions(map) {
    var directionsDisplay = new google.maps.DirectionsRenderer({
        map: map
    });
    var directionsService = new google.maps.DirectionsService;
    directionsDisplay.setMap(map);
    directionsDisplay.setPanel(document.getElementById('right-panel'));
    // Set destination, origin and travel mode.
    var request = {
        destination: end,
        origin: start,
        travelMode: google.maps.TravelMode.TRANSIT
    };
    // Pass the directions request to the directions service.
    var directionsService = new google.maps.DirectionsService();
    directionsService.route(request, function (response, status) {
        if (status == google.maps.DirectionsStatus.OK) {
            // Display the route on the map.
            directionsDisplay.setDirections(response);
        }
    });
}
$(document).ready(function () {
    $("#builder").click(function () {
        directions(map);
        $(this).fadeOut(1000);
        $('#right-panel').fadeIn(1500);
        setTimeout(function () {
            $('.adp-warnbox').fadeOut(2000);
        }, 5000);
    });
    //Скрипт для заявки на дзвінок
    $('#call').click(function () {
        if (!is_click_call) {
            is_click_call = true;
            $.ajax({
                url: "/telephony/add_call/" + user_id + "/" + id,
                type: "GET",
                success: function (data) {
                    if (data == "1") {
                        $('.cont_button').append('<h3>Запит відправлено</h3>');
                        setTimeout(function () {
                            $('h3').fadeOut(100)
                        }, 5000)
                    }
                }
            });
        }
    });
    //Скрипт для зміни стану виконання
    $('#confirm').click(function () {
        if (!is_click_call_conf) {
            is_click_call_conf = true;
            $.ajax({
                url: "/tracker/confirm_tracker/" + id,
                type: "GET",
                success: function (data) {
                    if (data == "1") {
                        $('.cont_button').append('<h3>Запит відправлено</h3>');
                        setTimeout(function () {
                            $('h3').fadeOut(100)
                        }, 5000)
                    }
                }
            });
        }
    })
});