<template>
  <div>
    <Error404 v-if="verificar(showSection)" />
    <div v-else class="container">
      <div class="row">
        <div class="col-md-9 col-sm-12">
          <h1 class="my-4">{{ noticias[position].titulo }}</h1>
          <hr width="90%" />
          <p>
            <b-icon icon="clock"></b-icon> Posteado el
            {{ noticias[position].fecha | fechaFormat }}
          </p>
          <hr width="90%" />
          <img
            :src="noticias[position].img_portada"
            class="shadow rounded-lg sticky-post-img"
            alt="..."
          />
          <hr width="90%" />
          <prism
            v-html="noticias[position].contenido"
            class="pre px-4 pt-4 mb-4 text-justify bg-light rounded-lg shadow"
          ></prism>
        </div>
        <div class="col-md-3 col-sm-12">
          <b-card
            title="Buscar"
            class="animate__animated animate__backInRight bg-opaco my-4 border-0 shadow"
            sub-title="Noticias"
          >
            <b-card-text>
              <b-input-group class="mt-3">
                <b-form-input
                  v-model="searchText"
                  placeholder="Buscar Noticia..."
                ></b-form-input>
                <b-input-group-append>
                  <router-link
                    :to="{
                      name: 'ListaNoticias',
                      params: { word: searchText }
                    }"
                    class="btn btn-info"
                    ><b-icon icon="search"></b-icon
                  ></router-link>
                </b-input-group-append>
              </b-input-group>
            </b-card-text>
          </b-card>

          <b-card
            title="Categorias"
            class="animate__animated animate__backInRight bg-opaco my-4 border-0 shadow"
            sub-title="Más noticias"
          >
            <b-card-text>
              <div class="row">
                <div class="col-md-6">
                  <p><small>Gatos</small></p>
                  <p><small>Perros</small></p>
                  <p><small>Cuidados</small></p>
                </div>
                <div class="col-md-6">
                  <p><small>Alimentos</small></p>
                  <p><small>Conducta</small></p>
                  <p><small>Limpieza</small></p>
                </div>
              </div>
            </b-card-text>
          </b-card>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { myMixins } from "@/mixins.js";
import Error404 from "@/components/Error404";
import "prismjs/themes/prism.css";
import Prism from "vue-prism-component";

export default {
  name: "NoticiaDetail",
  components: {
    Error404,
    Prism
  },
  data() {
    return {
      noticias: [],
      showSection: true,
      position: -1,
      searchText: ""
    };
  },
  filters: {
    fechaFormat(value) {
      let meses = [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre"
      ];
      let fechaFormat = new Date(Date.parse(value));
      let day = fechaFormat.getDate();
      let month = meses[fechaFormat.getMonth()];
      let year = fechaFormat.getFullYear();
      return day + " de " + month + ", " + year;
    }
  },
  mixins: [myMixins],
  methods: {
    verificar(showSection) {
      for (let i = 0; i < this.noticias.length; i++) {
        if (this.$route.params.noticiaId == this.noticias[i].id) {
          showSection = false;
          this.position = i;
        }
      }
      return showSection;
    }
  },
  created() {
    this.scrollBehavior(), this.getNoticias();
  }
};
</script>

<style scoped>
.sticky-post-img {
  max-height: 400px;
  height: 100%;
  width: 100%;
  display: block;
  object-fit: cover;
  object-position: center center;
}
.pre {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  white-space: pre-line;
}
.bg-opaco {
  background-color: rgba(247, 247, 247, 0.4) !important;
}
</style>
