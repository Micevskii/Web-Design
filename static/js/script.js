
    $(document).ready(function(){
    $(window).scroll(function(){
        if($(window).scrollTop() > 70) {
            $(".fixed-top").css({"background-color": "#172D44", "opacity": "95%"});
        }
        else{
            $(".fixed-top").css({"background-color":"transparent"});
        }
    })
})

    const counts = document.querySelectorAll('.count');
    const speed = 97;

    function startCounter(counter) {
    function upDate() {
        const target = Number(counter.getAttribute('data-target'));
        const count = Number(counter.innerText);
        const inc = target / speed;
        
        if (count < target) {
            counter.innerText = Math.floor(count + inc);
            setTimeout(upDate, 15);
        }
    }
    upDate();
    }

    const observe = new IntersectionObserver((entries, observe) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            console.log('Counter in view:', entry.target); 
            startCounter(entry.target);
            observe.unobserve(entry.target); 
        }
    });
    }, { threshold: 0.5 }); 

    counts.forEach(counter => {
    observe.observe(counter);
    console.log('Observing:', counter);
});



    const the_animation = document.querySelectorAll('.animation')

    const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('scroll-animation')
                }
            })
        },
        { threshold: 0.1
        });
    //
    for (let i = 0; i < the_animation.length; i++) {
        const elements = the_animation[i];

        observer.observe(elements);
    }

    $('#play-video').on('click', function(e){
        e.preventDefault();
        $('#video-overlay').addClass('open');
        $("#video-overlay").append('<iframe width="760" height="550" src="https://www.youtube.com/embed/cIspo11v3As?si=Aq3ARuAY9z0QYRRh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>');
    });

    $('.video-overlay, .video-overlay-close').on('click', function(e){
        e.preventDefault();
        close_video();
    });

    $(document).keyup(function(e){
        if(e.keyCode === 27) { close_video(); }
    });

    function close_video() {
        $('.video-overlay.open').removeClass('open').find('iframe').remove();
    };



    let items = document.querySelectorAll('.carousel-item-gallery')

    items.forEach((el) => {
        const minPerSlide = 4
        let next = el.nextElementSibling
        for (var i=1; i<minPerSlide; i++) {
            if (!next) {
                // wrap carousel by using first child
                next = items[0]
            }
            let cloneChild = next.cloneNode(true)
            el.appendChild(cloneChild.children[0])
            next = next.nextElementSibling
        }
    })

setTimeout(function(){
    $('#message').fadeOut('slow');
}, 1500);

function openSearch() {
    document.getElementById('searchOverlay').style.display = 'flex';
    document.getElementById('wtf').style.display = 'none';
    document.getElementById('title').style.display = 'none';
}

// Function to close the overlay (optional)
function closeSearch() {
    document.getElementById('searchOverlay').style.display = 'none';
    document.getElementById('wtf').style.display = 'block';
    document.getElementById('title').style.display = 'flex';

}



const c = document.querySelector('.pagi')
const indexs = Array.from(document.querySelectorAll('.index'))
let cur = -1
indexs.forEach((index, i) => {
  index.addEventListener('click', (e) => {
    // clear
    c.className = 'container'
    void c.offsetWidth; // Reflow
    c.classList.add('open')
    c.classList.add(`i${i + 1}`)
    if (cur > i) {
      c.classList.add('flip')
    }
    cur = i
  })
})





function translateContent(targetLanguage) {
        const textToTranslate = document.getElementById('content').innerText; // Get text to translate

        fetch('/translate/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}', // Include CSRF token for security
            },
            body: JSON.stringify({
                text: textToTranslate,
                target_language: targetLanguage
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.translated_text) {
                document.getElementById('content').innerText = data.translated_text; // Update the content with the translated text
            } else {
                console.error(data.error);
            }
        })
        .catch(error => console.error('Error:', error));
}

 // JavaScript to toggle the visibility and transition of language buttons
 document.getElementById('toggleLanguageButtons').addEventListener('click', function() {
    var languageButtons = document.getElementById('languageButtons');
    var globe = document.getElementById('globe');


    if (languageButtons.classList.contains('show-buttons')) {
        // Hide buttons by removing the 'show-buttons' class
        languageButtons.classList.remove('show-buttons');
      


        // Delay hiding the buttons to allow the transition to finish
        setTimeout(function() {
            languageButtons.style.display = 'none';
        }, 400); // Match the duration of the CSS transition (0.4s)
    } else {
        // Show buttons and apply the 'show-buttons' class

        languageButtons.style.display = 'flex';
        setTimeout(function() {
            languageButtons.classList.add('show-buttons');
        }, 10); // Slight delay to ensure the display change happens first
    }
});