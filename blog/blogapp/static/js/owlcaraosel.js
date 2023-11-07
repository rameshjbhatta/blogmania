<script>
    $(document).ready(function(){
        $('.owl-carousel').owlCarousel({
            loop: true, // Infinite loop
            margin: 10, // Margin between items
            nav: true, // Show navigation arrows
            autoplay: true, // Autoplay the carousel
            responsive:{
                0:{
                    items: 1 // Number of items to show on small screens
                },
                768:{
                    items: 2 // Number of items to show on medium screens
                },
                992:{
                    items: 4 // Number of items to show on large screens
                }
            }
        })
    })
</script>