$(function(){
    $(document).ready(function(){
        get_entry("Short Story");
        $(".type").on({
            click: function(){
                $(this).parent().children().removeClass("active1");

                $(this).addClass("active1");
                var id = $(this).attr('id');
                get_entry(id);
                //$(this).removeClass("active");
            }         
        });
    });

    function get_entry(id) {
        $.ajax({
            url : "/creative/get-entry",
            type : "GET",
            data : {tag_type : id},
            success : function(entries) {
                ent = entries['entries']
                $(".entries").html("")
                for(i=0;i<ent.length;i++){
                    entry_div = document.createElement("DIV")
                    entry_div.setAttribute("class", "entry-div")
                    n = document.createElement("H2");
                    n.innerHTML = ent[i]["name"];
                    n.setAttribute("class","entry-text")
                    s = document.createElement("H5");
                    s.innerHTML = ent[i]["status"];
                    s.setAttribute("class","entry-text")

                    link = document.createElement("A");
                    link.setAttribute("href", ent[i]["url"]);
                    entry_div.appendChild(n);
                    entry_div.appendChild(s);
                    link.appendChild(entry_div)

                    $(".entries").append(link)
                }
            },
            error : function(xhr, errmsg, err){
                alert("Sorry");
            }
        });

    };

});