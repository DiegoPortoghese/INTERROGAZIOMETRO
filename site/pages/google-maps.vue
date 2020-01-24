<template>
  <div>
    <div>
      <h2>Dove si trova la stanza?</h2>
      <label style="width: 400px">
        <gmap-autocomplete @place_changed="setPlace" style="width: 400px" placeholder="digita la posizione">
        </gmap-autocomplete>
      </label>
      <br/>

    </div>
    <br>
    <gmap-map
      :center="center"
      :zoom="12"
      style="width:100%;  height: 400px;"
    >
      <gmap-marker
        :key="marker"
        v-model="marker"
        :position="marker.position"
        @click="center=marker.position"
      ></gmap-marker>
    </gmap-map>
  </div>
</template>

<script>
export default {
  name: "GoogleMap",
  data() {
    return {
      // default to Montreal to keep it simple
      // change this to whatever makes sense
      center: { lat: 0.0, lng: -0.0 },
      marker: { position:null },
      currentPlace: null,
    };
  },

  mounted() {
    this.geolocate();
  },

  methods: {
    // ARRAY GOOGLE MAPS API: https://developers.google.com/places/web-service/autocomplete https://developers.google.com/places/web-service/details
    // receives a place object via the autocomplete component
    setPlace(place) {
      this.currentPlace = place;
      try{
          const marker_gen = {
            lat: this.currentPlace.geometry.location.lat(),
            lng: this.currentPlace.geometry.location.lng()
          };
          //this.m = marker;
          this.marker = {position: marker_gen};
          this.center = marker_gen;
          console.log('formatted_address'+this.currentPlace.formatted_address) // full address
          console.log('6: '+this.currentPlace.address_components[6].long_name) // 6 Country
          console.log('5:'+this.currentPlace.address_components[5].long_name) // 5 Regione
          console.log('4:'+this.currentPlace.address_components[4].long_name) // 4 Provincia
          console.log('3:'+this.currentPlace.address_components[3].long_name) // 3 comune
          console.log(this.marker) // 3 comune
          this.currentPlace = null;
          
      }catch (e){
        console.log(e)
      }
    },
    addMarker() {
      
    },
    geolocate: function() {
      navigator.geolocation.getCurrentPosition(position => {
        this.center = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };
      });
    }
  }
};
</script>