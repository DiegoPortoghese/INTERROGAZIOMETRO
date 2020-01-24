<template>
  <div class="container mt-4" >
    <h1> About </h1>
    <p> 
      Lorem ipsum dolor sit amet consectetur adipisicing elit. 
      Eum dolore incidunt nobis illo! Temporibus debitis voluptatem corporis 
      ullam sed reprehenderit eum eaque sapiente modi, voluptatum quam amet 
      fuga iure doloribus! 
    </p>
  </div>
</template>

<script>
export default {
  middleware: 'auth',
  asyncData () {
    return new Promise((resolve) => {
      setTimeout(function () {
        resolve();
      }, 5000)
    })
  }
}
</script>

