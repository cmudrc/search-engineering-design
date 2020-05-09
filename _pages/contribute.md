---
title: Contribute
layout: splash
permalink: /contribute/

header:
  overlay_color: "#000"
  overlay_filter: "0.5"  
  overlay_image: /assets/images/books.jpg
  caption: "Photo by [Patrick Tomasso](https://unsplash.com/@impatrickt) on [Unsplash](https://unsplash.com/)"
excerpt: ""

---

# Report a bug
Did you something go wrong when you tried to use this search engine? Let us know here!

<div class="container mt-5 mb-5">
    <form>
        <div class="form-group">
            <label for="email">What is your email address?</label>
            <input class="form-control" id="email"
                   placeholder="asdf@asdf.org">
        </div>

        <div class="form-group">
            <label for="report">What went wrong?</label>
            <input class="form-control" id="report" placeholder="Something spooky">
        </div>

        <div class="form-group">
            <label for="repro">How can we reproduce the issue?</label>
            <textarea class="form-control" id="repro" rows="3" placeholder="Click some buttons"></textarea>
        </div>

        <button id="submitbug" class="btn btn-primary">Submit</button>
    </form>
</div>
<br/>

# Recommend a journal
Is there a journal that you'd like to see in this search engine? Recommend it here!


<div class="container mt-5 mb-5">
    <form>
        <div class="form-group">
            <label for="email2">What is your email address?</label>
            <input class="form-control" id="email2"
                   placeholder="asdf@asdf.org">
        </div>

        <div class="form-group">
            <label for="where">Where can we find this journal?</label>
            <input class="form-control" id="where" placeholder="https://asdf.org">
        </div>

        <div class="form-group">
            <label for="why">Why do you think it should be added?</label>
            <textarea class="form-control" id="why" rows="3" placeholder="Because its awesome!"></textarea>
        </div>

        <button id="submitjournal" class="btn btn-primary">Submit</button>
    </form>
</div>
<br/>

# Contributing
Want to help develop this website? Contribute on [GitHub](https://github.com/THREDgroup/search-engineering-design).

# Contact
Email Chris McComb by clicking [here](mailto:mccomb@psu.edu).

<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
<script>        
    let token = "eb0f683d0e93672d148f" + "83f581f4c12ae83f02b4";

    function clean_non_ascii(stringystring) {
        return stringystring.replace("’", "'").replace("”", '"').replace("“", '"');
    }

    function bug_report(event) {
        event.preventDefault();

        // Get the details
        let email = clean_non_ascii($("#email").val());
        let report = clean_non_ascii($("#report").val());
        let repro = clean_non_ascii($("#repro").val());

        $.ajax({
                url: 'https://api.github.com/repos/thredgroup/search-engineering-design/issues',
                headers: {'Authorization': 'token ' + token},
                type: "POST",
                data: '{"title": "' + report + '", "body": "' + repro + '. Recommended by ' + email +'"}',
                success: function (results) {
                    alert("This bug has been reported!");
                        $("#email").val("");
                        $("#report").val("");
                        $("#repro").val("");
                },
                error: function (results) {
                    alert("Sorry, I ran into an issue: <code>" + JSON.stringify(results) + "</code>");
                }
            });

    }
    
        function new_journal_request(event) {
            event.preventDefault();
    
            // Get the details
            let email = clean_non_ascii($("#email2").val());
            let where = clean_non_ascii($("#where").val());
            let why = clean_non_ascii($("#why").val());
    
            $.ajax({
                    url: 'https://api.github.com/repos/thredgroup/search-engineering-design/issues',
                    headers: {'Authorization': 'token ' + token},
                    type: "POST",
                    data: '{"title": "' + where + '", "body": "' + why + '. Recommended by ' + email +'"}',
                    success: function (results) {
                        alert("This recommendation has been logged!");
                        $("#email2").val("");
                        $("#where").val("");
                        $("#why").val("");
                    },
                    error: function (results) {
                        alert("Sorry, I ran into an issue: <code>" + JSON.stringify(results) + "</code>");
                    }
                });
    
        }

    $("#submitbug").on('click', bug_report)
    $("#submitjournal").on('click', new_journal_request)

</script>
