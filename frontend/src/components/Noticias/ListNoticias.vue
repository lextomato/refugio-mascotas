<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-md-8 col-sm-12 bg-light rounded-lg shadow my-4">
          <h1 class="my-4">
            Noticias de la Comunidad <small>Casa Adoptiva</small>
          </h1>
          <hr width="90%" />

          <div v-if="error" class="error">
            {{ error }}
          </div>

          <div v-if="loading" class="d-flex justify-content-center mb-3">
            <b-spinner
              lstyle="width: 3rem; height: 3rem;"
              label="Large Spinner"
            ></b-spinner>
          </div>

          <!-- Notices -->
          <div v-if="!loading">
            <div
              v-for="noticia in paginador(searchFilt(noticias))"
              :key="noticia.id"
              class="animate__animated animate__fadeIn"
            >
              <div class="row mb-3">
                <b-col cols="12" class="text-center">
                  <h5 class="font-italic font-weight-bold">
                    {{ noticia.titulo }}
                  </h5>
                </b-col>
              </div>
              <div class="row">
                <div class="col-md-7">
                  <router-link
                    :to="{
                      name: 'noticia-detail',
                      params: { noticiaId: noticia.id }
                    }"
                  >
                    <img
                      class="img-fluid rounded mb-3 mb-md-0 sticky-list-img"
                      :src="noticia.img_portada"
                      alt=""
                    />
                  </router-link>
                </div>
                <div class="col-md-5">
                  <h6>
                    <span class="badge badge-secondary"
                      ><b-icon icon="clock"></b-icon>
                      {{ noticia.fecha | fechaFormat }}</span
                    >
                    <span class="badge badge-secondary">{{
                      noticia.categoria
                    }}</span>
                  </h6>
                  <p class="text-justify text-muted">
                    {{ noticia.contenido | firts144 | striphtml }}...
                  </p>
                  <router-link
                    class="btn btn-outline-info"
                    :to="{
                      name: 'noticia-detail',
                      params: { noticiaId: noticia.id }
                    }"
                    ><b-icon icon="file-richtext"></b-icon> Ver
                    Noticia</router-link
                  >
                </div>
                <hr width="90%" />
              </div>
            </div>
            <!-- /.row -->

            <!-- Pagination -->
            <div class="mt-3">
              <b-pagination
                align="center"
                v-model="page"
                :per-page="perPage"
                pills
                :total-rows="rows"
              ></b-pagination>
            </div>
            <!-- /.div -->
          </div>
        </div>
        <div class="col-md-4 col-sm-12 animate__animated animate__backInRight">
          <div class="col-md-12 mt-4 mb-2 mr-3 py-3 shadow bg-light rounded">
            <h2 class="font-italic">Noticias</h2>
          </div>

          <b-card
            title="Buscar"
            class="bg-opaco mb-2 border-0 shadow"
            sub-title="Noticias"
          >
            <b-card-text>
              <b-input-group class="mt-3">
                <b-form-input
                  v-model="searchText"
                  placeholder="Palabras claves..."
                ></b-form-input>
                <b-input-group-append>
                  <b-button variant="info" disabled
                    ><b-icon icon="search"></b-icon
                  ></b-button>
                </b-input-group-append>
              </b-input-group>
              <br />
              <span
                v-for="(word, index) in words(searchText)"
                :key="index"
                class="mx-1 badge badge-secondary"
                >{{ word }}</span
              >
            </b-card-text>
          </b-card>

          <b-card
            title="Categorias"
            class="bg-opaco mb-2 border-0 shadow"
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
import "prismjs/themes/prism.css";
import Prism from "vue-prism-component";

export default {
  name: "NoticiaDetail",
  components: {
    Prism
  },
  data() {
    return {
      noticias: [],
      position: -1,
      page: 1,
      perPage: 4,
      rows: 0,
      loading: true,
      error: null,
      searchText: ""
    };
  },
  watch: {
    // call again the method if the route changes
    $route: "getNoticias"
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
      return day + " " + month + ", " + year;
    },
    firts144(value) {
      let reduc = value.substring(0, 143);
      return reduc;
    },
    striphtml(value) {
      let div = document.createElement("div");
      div.innerHTML = value;
      let text = div.textContent || div.innerText || "";
      return text;
    }
  },
  mixins: [myMixins],
  methods: {
    searchExist() {
      if (this.$route.params.word) {
        this.searchText = this.$route.params.word;
      }
    },
    paginador(noticias) {
      let filtrados = [];
      for (let i = 0; i < noticias.length; i++) {
        filtrados[i] = noticias[i];
      }

      this.rows = filtrados.length;

      const indiceInicio = (this.page - 1) * this.perPage;
      const indiceFinal =
        indiceInicio + this.perPage > filtrados.length
          ? filtrados.length
          : indiceInicio + this.perPage;
      return filtrados.slice(indiceInicio, indiceFinal);
    }
  },
  created() {
    this.scrollBehavior(), this.getNoticias(), this.searchExist();
  }
};
</script>

<style scoped>
.sticky-list-img {
  max-height: 240px;
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
