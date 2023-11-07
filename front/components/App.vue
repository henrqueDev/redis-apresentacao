<template>
  <div id="app">
    
    <b-img alt="Vue Menu" class="mt-0 pt-0" src="@/assets/nasaaa.png">
    </b-img>

    <ISSRadar />

  </div>
</template>
<script>
import '@/assets/css/App.css'
import ISSRadar from '@/components/ISSRadar'


export default {
  name: 'App',
  components: {
    ISSRadar
  },
  data(){
    return{
      bgImg: ""
    }
  }
}
</script>