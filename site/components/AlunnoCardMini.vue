<template>
  <div :class="'card flex-row flex-wrap shadow rounded '" >
    <div class="card-header border-0 raunded">
        <img class="rounded-circle " v-if="alunno.avatar_image == ''" src="//placehold.it/70" alt="">
        <img class="rounded-circle " v-if="alunno.avatar_image != ''" :src="'http://localhost:8000/media/'+alunno.avatar_image" width="70px" height="70px" alt="">

    </div>
    <div class="card-block px-2">
        <h6 class="card-title" style="padding-top:12px">{{alunno.first_name+" "+alunno.last_name | truncate(16) }}</h6>
        <p class="card-text" style="font-size:15px;"><b>{{alunno.nome_materia_turno}}</b><br>{{alunno.data}}</p>
    </div>
    
  </div>
</template>
<style>

</style>
<script>

export default {
    props: ["alunno"],
    filters:{
      truncate(string, value) {
        return (string || '').substring(0, value) 
      }
    },
    methods:{
      viewRoom(roomId){
        window.location = '/rooms/'+roomId
        
      }

    }
};
</script>

