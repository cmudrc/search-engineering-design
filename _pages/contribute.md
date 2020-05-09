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

        <button id="submitbug" class="btn btn-primary">Submit</button>
    </form>
</div>
<br/>

# Recommend a journal
Is there a journal that you'd like to see in this search engine? Recommend it here!


<div class="container mt-5 mb-5">
    <form>
        <div class="form-group">
            <label for="title">What is your email address?</label>
            <input class="form-control" id="email"
                   placeholder="asdf@asdf.org">
        </div>

        <div class="form-group">
            <label for="year">Where can we find this journal?</label>
            <input class="form-control" id="report" placeholder="https://thred.group/search-engineering-design/contribute/">
        </div>

        <div class="form-group">
            <label for="year">Why do you think it should be added?</label>
            <input class="form-control" id="report" placeholder="It is awesome!">
        </div>

        <button id="submit" class="btn btn-primary">Submit</button>
    </form>
</div>
<br/>

# Contributing
Want to help develop this website? Contribute on [GitHub](https://github.com/THREDgroup/search-engineering-design).

# Contact
Email Chris McComb by clicking [here](mailto:mccomb@psu.edu).

<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
<script>
    function clean_non_ascii(stringystring) {
        return stringystring.replace("’", "'").replace("”", '"').replace("“", '"');
    }

    function bug_report(event) {
        event.preventDefault();

        // Get the details
        let email = clean_non_ascii($("#email").val());
        let report = clean_non_ascii($("#report").val());

        $.ajax({
                url: 'https://api.github.com/repos/thredgroup/search-engineering-design/issues',
                headers: {'Authorization': 'token 2f5e2123640cb7b1b3ffc99d1263f66f77c7b521'},
                type: "POST",
                data: '{"title": "' + report + '", "body": "Recommended by ' + email +'"}',
                success: function (results) {
                    alert("Your bug has been reported");
                },
                error: function (results) {
                    alert("Sorry, I ran into an issue" + results);
                }
            });

    }

    $("#submitbug").on('click', bug_report)

</script>
