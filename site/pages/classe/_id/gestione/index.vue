<template>
<main>
    <div class="nav-scroller bg-white box-shadow">
      <nav class="nav nav-underline">
        <a class="nav-link active" href="gestione/">Principale</a>
        <a class="nav-link" href="../gestione/note">Note</a>
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
        <h2 class="mb-3 display-4">{{classe.nome}}</h2>
      </div>
      <div class="col-md-6 mb-4">
        <img
          v-if="preview"
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          :src="preview"
          alt
        >
        <img
          v-else
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          :src="classe.immagine_copertina"
        >
      </div>
      <div class="col-md-4">
        <form @submit.prevent="submitRecipe">
          <label for>Sezione</label>
          <b-form-input id="inputSezione" v-model="classe.sezione" type="text" placeholder="esempio: A , B , C " ></b-form-input>
          <label for>Anno</label>
          <b-form-group >
            <b-form-radio v-model="classe.anno" name="some-radios" value="1">Primo</b-form-radio>
            <b-form-radio v-model="classe.anno" name="some-radios" value="2">Secondo</b-form-radio>
            <b-form-radio v-model="classe.anno" name="some-radios" value="3">Terzo</b-form-radio>
            <b-form-radio v-model="classe.anno" name="some-radios" value="3">Quarto</b-form-radio>
            <b-form-radio v-model="classe.anno" name="some-radios" value="3">Quinto</b-form-radio>
          </b-form-group>
          <div class="form-group">
            <label for>Nome Personalizzato della classe</label>
            <input type="text" class="form-control" v-model="classe.nome">
          </div>
          <div class="form-group">
            <label for>Breve descrizione della classe</label>
            <input v-model="classe.descrizione" type="text" class="form-control">
          </div>
          <div class="form-group">
            <label for>Foto Copertina</label>
            <input type="file" name="file" @change="onFileChange">
          </div>
          <div class="row">
            <div class="col-md-6">
            </div>
            <div class="col-md-6">
            </div>
          </div>
          <button type="submit" class="btn btn-primary">Modifica</button>
        </form>
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
    onFileChange(e) {
      let files = e.target.files || e.dataTransfer.files;
      if (!files.length) {
        return;
      }
      this.classe.immagine_copertina = files[0];
      this.createImage(files[0]);
    },
    createImage(file) {
      // let image = new Image();
      let reader = new FileReader();
      let vm = this;
      reader.onload = e => {
        vm.preview = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    async submitRecipe() {
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      let formData = new FormData();
      // for (let data in this.classe) {
      //   formData.append(data, this.classe[data]);
      // }
      formData.append('sezione',this.classe.sezione)
      formData.append('anno',this.classe.anno)
      formData.append('nome',this.classe.nome)
      formData.append('descrizione',this.classe.descrizione)
      formData.append('immagine_copertina',this.classe.immagine_copertina)
      try {
        let response = await this.$axios.$put(`api/classe/${this.classe.id}/`, formData, config);
        console.log(response)
        var string_route = "/classe/"+response.id+"/gestione/Orario"
        this.$router.push(string_route);
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>