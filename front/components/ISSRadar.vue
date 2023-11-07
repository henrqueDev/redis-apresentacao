<template>
    <div id="ISS">
        <h1 style="color: blue; font-size:40px; margin-bottom:4rem;">Estação Espacial Internacional</h1>
        <p style="color: red; font-size:30px;"> 
            
            {{ altitude }} </p>


        <p style="color: red; font-size:30px;"> 
            
            {{ velocidadeNaOrbita }} </p>
        
  <l-map  class="radar" :zoom="zoom" :center="center">
    <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
    <l-marker :lat-lng="markerLatLng"></l-marker>
  </l-map>
    </div>
</template>


<script>
/* eslint-disable */
import L from 'leaflet'
import {LMap, LTileLayer, LMarker} from 'vue2-leaflet';
import axios from 'axios'
export default {
    name:'ISSRadar',
    components: {
    L,
    LMap,
    LTileLayer,
    LMarker
  },
    data () {
        return {
            url: `http://{s}.tile.osm.org/{z}/{x}/{y}.png`,
            attribution:
                '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            zoom: 13,
            center: L.latLng(0, 0),
            markerLatLng: L.latLng(0, 0),
            MyMap: null,
            refresh: false,
            velocidadeNaOrbita: 'Velocidade na orbita: 0 Km/h',
            altitude: ' Altitude: 0 km'
    };
  },
  mounted(){
        this.moveUp()
      },
  methods: {
     moveUp(){
        setInterval(async() =>{
            let pos = await axios.get('http://127.0.0.1:5000/iss')
            console.log(pos)
            
            
    	    this.markerLatLng = L.latLng(pos.data.latitude, pos.data.longitude)
            this.center= L.latLng(pos.data.latitude , pos.data.longitude)
            this.velocidadeNaOrbita = `Velocidade na orbita: ${pos.data.velocity.toFixed(2)} Km/h`
            this.altitude = `Altitude: ${900 + pos.data.altitude} Km`

            return 0

        },1000)
    }
  }
}
</script>

<style>

#ISS{
    height:90vh;
    width:100vw;
}
.radar{
    width:100%;
    height: 100%;
}

</style>