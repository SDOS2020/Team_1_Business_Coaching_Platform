<template>
  <div class="home">
    {{ msg }}
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  data(){
    return {
      msg : 'hello world!'
    }
  }
}
</script>
