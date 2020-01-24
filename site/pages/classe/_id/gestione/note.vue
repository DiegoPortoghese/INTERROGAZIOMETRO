<template>
<main>
    <div class="nav-scroller bg-white box-shadow">
      <nav class="nav nav-underline">
        <a class="nav-link" href="../gestione/">Principale</a>
        <a class="nav-link active" href="../gestione/note">Note</a>
        <a class="nav-link" href="../gestione/orario">Orario</a>
        <a class="nav-link" href="../gestione/evento">Interrogazioni</a>
        <a class="nav-link" href="../gestione/conferme">
          Conferme
          <span class="badge badge-pill bg-light align-text-bottom"></span>
        </a>
      </nav>
    </div>

<div class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <b-col sm="12">
        <b-form-textarea
            id="textarea-small"
            size="sm"
            placeholder="Small textarea"
            style="height:500px"
            v-model="classe.note"
      ></b-form-textarea>
          <button class="btn btn-block btn-success" v-on:click="submitRecipe">Salva</button>
    </b-col>

      </div>
    </div>
  </div>

</main>

  

</template>
<script>
export default {
  head() {
    return {
      title: "Dashboard classe"
    };
  },
  data() {
    return {
      classe: {
        sezione: '',
        anno:0,
        nome: "",
        descrizione: "",
        note:""
      },
      preview: ""
    };
  },
  async asyncData({ $axios, params }) {
      try {
        let classe = await $axios.$get(`api/classe/${params.id}/`);
        return { classe };
      } catch (e) {
        return { classe: [] };
      }
    },
  methods: {
    
    async submitRecipe() {
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      let formData = new FormData();
      // for (let data in this.classe) {
      //   formData.append(data, this.classe[data]);
      // }
      formData.append('note',this.classe.note)
      try {
        let response = await this.$axios.$put(`api/classe/${this.classe.id}/`, formData, config);
        console.log(response)
        var string_route = "/classe/"+response.id+"/gestione/Orario"
        location.reload()
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>