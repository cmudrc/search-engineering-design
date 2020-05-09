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
            <label for="title">What is your email address?</label>
            <input class="form-control" id="email"
                   placeholder="asdf@asdf.org">
        </div>

        <div class="form-group">
            <label for="year">What went wrong?</label>
            <input class="form-control" id="report" placeholder="Something spooky">
        </div>

        <button id="submit" class="btn btn-primary">Submit</button>
    </form>
</div>

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
            <input class="form-control" id="report" placeholder="Something spooky">
        </div>

        <div class="form-group">
            <label for="year">Why do you think it should be added?</label>
            <input class="form-control" id="report" placeholder="Something spooky">
        </div>

        <button id="submit" class="btn btn-primary">Submit</button>
    </form>
</div>

# Contributing
Want to help develop this website? Contribute on [GitHub](https://github.com/THREDgroup/search-engineering-design).

# Contact
Email Chris McComb by clicking [here](mailto:mccomb@psu.edu).

<script>
    function commit_to_github(event) {
        event.preventDefault();

        function clean_non_ascii(stringystring) {
            return stringystring.replace("’", "'").replace("”", '"').replace("“", '"');
        }

        // Get the details
        let title = clean_non_ascii($("#title").val());
        let authors = clean_non_ascii($("#authors").val());
        let type = clean_non_ascii($("#type").val());
        let venue = clean_non_ascii($("#venue").val());
        let year = clean_non_ascii($("#year").val());
        let abstract = clean_non_ascii($("#abstract").val());

        // Set filename
        let filename = year + "-01-01-" + title.replace(/[^A-Za-z0-9]/g, '') + ".md";

        // Format file contents
        let data = '---\n';
        data += 'layout: pub\n';
        data += "type: " + type + "\n";
        data += 'title: "' + title + '"\n';
        data += 'authors: ["' + authors.split(", ").join(",").split(",").join('", "') + '"]\n';
        data += 'venue: ' + venue + "\n";
        data += 'year: ' + year + '\n';
        data += 'accepted: true\n---\n';
        data += abstract;

        console.log(filename);
        console.log(data);

        // Check encoding
        let clean = false;
        let encoded = '';
        try {
            encoded = window.btoa(data);
            clean = true;
        }
        catch(err) {
            clean = false;
            $(".container").prepend("<div class=\"alert alert-danger alert-dismissible\">\n" +
                "    <a href=\"#\" class=\"close\" data-dismiss=\"alert\" aria-label=\"close\">&times;</a>\n" +
                "    <strong>Oops!</strong> There's something wrong with the information that you entered.\n" +
                "<br/><code>" + err.message + "</code>" +
                "  </div>");
        }

        if(clean) {
            $.ajax({
                url: 'https://api.github.com/repos/thredgroup/thredgroup.github.io/contents/_posts/' + filename,
                headers: {'Authorization': 'token THIS_IS_THE_TOKEN'},
                type: "PUT",
                data: '{"message": "New paper", "content": "' + encoded + '"}',
                success: function (results) {
                    $(".container").prepend("<div class=\"alert alert-success alert-dismissible\">\n" +
                        "    <a href=\"#\" class=\"close\" data-dismiss=\"alert\" aria-label=\"close\">&times;</a>\n" +
                        "    <strong>Success!</strong> A new publication was successfully added to the website.\n" +
                        "  </div>");
                    $("html, body").animate({scrollTop: 0}, "slow");

                    // Clear
                    $("#title").val("");
                    $("#authors").val("");
                    $("#venue").val("");
                    $("#year").val("");
                    $("#abstract").val("");
                },
                error: function (results) {
                    $(".container").prepend("<div class=\"alert alert-danger alert-dismissible\">\n" +
                        "    <a href=\"#\" class=\"close\" data-dismiss=\"alert\" aria-label=\"close\">&times;</a>\n" +
                        "    <strong>Oops!</strong> There was an issues adding this publication to the website.\n" +
                        "  </div>");
                    $("html, body").animate({scrollTop: 0}, "slow");
                }
            });
        }

    }

    $("#submit").on('click', commit_to_github)

</script>
