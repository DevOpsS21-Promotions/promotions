$(function () {

    // ****************************************
    //  U T I L I T Y   F U N C T I O N S
    // ****************************************

    // Updates the form with data from the response
    function update_form_data(res) {
        $("#promotion_id").val(res.id);
        $("#promotion_name").val(res.name);
        $("#promotion_promo_code").val(res.description);
        $("#promotion_description").val(res.description);
        $("#promotion_start_date").val(res.start_date);
        $("#promotion_end_date").val(res.end_date);
<<<<<<< HEAD
        $("#promotion_active").val(res.is_active);
=======
        if (res.is_active == true) {
            $("#promotion_active").val(true);
        } else {
            $("#promotion_active").val(false);
        }
>>>>>>> 120b5d8a43a1eb04e6bd6dc8c08249c074c9544f
    }

    /// Clears all form fields
    function clear_form_data() {
        $("#promotion_id").val("");
        $("#promotion_name").val("");
        $("#promotion_promo_code").val("");
        $("#promotion_description").val("");
        $("#promotion_start_date").val("");
        $("#promotion_end_date").val("");
        $("#promotion_active").val(true);
    }

    // Updates the flash message area
    function flash_message(message) {
        $("#flash_message").empty();
        $("#flash_message").append(message);
    }

    // ****************************************
    // Create a Promotion
    // ****************************************

    $("#create-btn").click(function () {
        
        var name = $("#promotion_name").val();
        var description = $("#promotion_description").val();
        var promo_code = $("#promotion_promo_code").val();
        var start_date = $("#promotion_start_date").val();
        var end_date = $("#promotion_end_date").val();
        var is_active = $("#promotion_active").val();
        if (is_active == "True") {
            is_active = true
        } else {
            is_active = false
        }

        var data = {
            "name": name,
            "description": description,
            "promo_code": promo_code,
            "start_date": start_date,
            "end_date": end_date,
            "is_active": is_active
        };

        flash_message(JSON.stringify(data))

        var ajax = $.ajax({
            type: "POST",
            url: "/promotions",
            contentType: "application/json",
            data: JSON.stringify(data),
        });

        ajax.done(function(res){
            update_form_data(res)
            flash_message("Success")
        });

        ajax.fail(function(res){
            flash_message(res.responseJSON.message)
        });
    });


    // ****************************************
    // Update a Promotion
    // ****************************************

    $("#update-btn").click(function () {

        var promotion_id = $("#promotion_id").val();
        var name = $("#promotion_name").val();
        var description = $("#promotion_description").val();
        var promo_code = $("#promotion_promo_code").val();
        var start_date = $("#promotion_start_date").val();
        var end_date = $("#promotion_end_date").val();
        var is_active = $("#promotion_active").val();
        if (is_active == "True") {
            is_active = true
        } else {
            is_active = false
        }

        var data = {
            "name": name,
            "description": description,
            "promo_code": promo_code,
            "start_date": start_date,
            "end_date": end_date,
            "is_active": is_active
        };

        var ajax = $.ajax({
                type: "PUT",
                url: "/promotions/" + promotion_id,
                contentType: "application/json",
                data: JSON.stringify(data)
            })

        ajax.done(function(res){
            update_form_data(res)
            flash_message("Success")
        });

        ajax.fail(function(res){
            flash_message(res.responseJSON.message)
        });

    });

    // ****************************************
    // Retrieve a Promotion
    // ****************************************

    $("#retrieve-btn").click(function () {

        var promotion_id = $("#promotion_id").val();

        var ajax = $.ajax({
            type: "GET",
            url: "/promotions/" + promotion_id,
            contentType: "application/json",
            data: ''
        })

        ajax.done(function(res){
            //alert(res.toSource())
            update_form_data(res)
            flash_message("Success")
        });

        ajax.fail(function(res){
            clear_form_data()
            flash_message(res.responseJSON.message)
        });

    });

    // ****************************************
    // Delete a Promotion
    // ****************************************

    $("#delete-btn").click(function () {
      
        var promotion_id = $("#promotion_id").val();

        var ajax = $.ajax({
            type: "DELETE",
            url: "/promotions/" + promotion_id,
            contentType: "application/json",
            data: '',
        })

        ajax.done(function(res){
            clear_form_data()
            flash_message("Promotion has been Deleted!")
        });
        
        ajax.fail(function(res){
            flash_message("Server error!")
        });
        
    });

    // ****************************************
    // Cancel a Promotion
    // ****************************************

    $("#cancel-btn").click(function () {

        var promotion_id = $("#promotion_id").val();
        
        var ajax = $.ajax({
            type: "PUT",
            url: "/promotions/" + promotion_id + "/cancel",
            contentType: "application/json",
            data: '',
        })

        ajax.done(function(res){
            clear_form_data()
            flash_message("Promotion has been Canceled!")
        });

        ajax.fail(function(res){
            flash_message("Server error!")
        });
    });

    // ****************************************
    // Clear the form
    // ****************************************

    $("#clear-btn").click(function () {
        $("#promotion_id").val("");
        clear_form_data()
    });

    // ****************************************
    // Search for a Promotion
    // ****************************************

    $("#search-btn").click(function () {

        var name = $("#promotion_name").val();
        var description = $("#promotion_description").val();
        var promo_code = $("#promotion_promo_code").val();
        var start_date = $("#promotion_start_date").val();
        var end_date = $("#promotion_end_date").val();

        var queryString = ""

        if (name) {
            queryString += 'name=' + name
        }
        if (description) {
            if (queryString.length > 0) {
                queryString += '&description=' + description
            } else {
                queryString += 'description=' + description
            }
        }
        if (promo_code) {
            if (queryString.length > 0) {
                queryString += '&promo_code=' + promo_code
            } else {
                queryString += 'promo_code=' + promo_code
            }
        }

        var ajax = $.ajax({
            type: "GET",
            url: "/promotions?" + queryString,
            contentType: "application/json",
            data: ''
        })

        ajax.done(function(res){
            //alert(res.toSource())
            $("#search_results").empty();
            $("#search_results").append('<table class="table-striped" cellpadding="10">');
            var header = '<tr>'
            header += '<th style="width:5%">ID</th>'
            header += '<th style="width:30%">Name</th>'
            header += '<th style="width:30%">Description</th>'
            header += '<th style="width:10%">Promo_Code</th>'
            header += '<th style="width:10%">Start_Date</th></tr>'
            header += '<th style="width:10%">End_Date</th></tr>'
            header += '<th style="width:5%">Is_Active</th></tr>'
            $("#search_results").append(header);
            var firstPromotion = "";
            for(var i = 0; i < res.length; i++) {
                var promotion = res[i];
                var row = "<tr><td>"+promotion._id+"</td><td>"+promotion.name+"</td><td>"+promotion.description+"</td><td>"+promotion.promo_code+"</td><td>"+promotion.start_date+"</td><td>"+promotion.end_date+"</td></tr>"+promotion.is_active+"</td></tr>";
                $("#search_results").append(row);
                if (i == 0) {
                    firstPromotion = promotion;
                }
            }

            $("#search_results").append('</table>');

            // copy the first result to the form
            if (firstPromotion != "") {
                update_form_data(firstPromotion)
            }

            flash_message("Success")
        });

        ajax.fail(function(res){
            flash_message(res.responseJSON.message)
        });

    });

})
