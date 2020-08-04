<template lang="html">
  <div>
    <div class="container">
      <div class="row">
        <div class="col-md-4 animate__animated animate__backInLeft">
          <div class="col-md-12 mt-4 mb-2 mr-3 py-3 shadow bg-light rounded">
            <h2 class="font-italic">Mascotas</h2>
          </div>
          <div class="col-md-12 mb-5 mr-3 shadow bg-light rounded">
            <b-button
              pill
              variant="outline-primary"
              @click="getOptions"
              class="my-3"
              ><b-icon icon="filter" aria-hidden="true"></b-icon
              >Filtros</b-button
            >
            <div class="row" v-if="vFiltro">
              <div class="col-md-6">
                <h5>
                  <span
                    class="badge badge-secondary align-middle text-center font-weight-bold shadow-sm p-1"
                    >No Adoptados</span
                  >
                </h5>
              </div>
              <div class="col-md-5 py-2 align-middle text-center">
                <b-form-checkbox
                  v-model="filtros.disp"
                  name="check-button"
                  switch
                ></b-form-checkbox>
              </div>
            </div>
            <div class="row" v-if="vFiltro">
              <div
                role="button"
                class="bt-hover col-md-1 align-middle text-center"
              >
                <b-icon
                  font-scale="1.5"
                  v-show="filtros.especie != ''"
                  role="button"
                  class="mx-auto btn-outline-danger align-middle"
                  @click="resetEspecie"
                  icon="x-square"
                  aria-hidden="true"
                ></b-icon>
              </div>
              <div class="col-md-5">
                <h5>
                  <span
                    class="badge badge-secondary align-middle text-center font-weight-bold shadow-sm p-1"
                    >Especie</span
                  >
                </h5>
              </div>
              <div class="col-md-5">
                <b-form-select
                  v-model="filtros.especie"
                  :options="especie(mascotas)"
                  class="mb-3"
                ></b-form-select>
              </div>
            </div>
            <div class="row" v-if="vFiltro">
              <div
                role="button"
                class="bt-hover col-md-1 align-middle text-center"
              >
                <b-icon
                  font-scale="1.5"
                  role="button"
                  v-show="filtros.raza != ''"
                  class="mx-auto btn-outline-danger"
                  @click="resetRaza"
                  icon="x-square"
                  aria-hidden="true"
                ></b-icon>
              </div>
              <div class="col-md-5">
                <h5>
                  <span
                    class="badge badge-secondary align-middle text-center font-weight-bold shadow-sm p-1"
                    >Raza</span
                  >
                </h5>
              </div>
              <div class="col-md-5">
                <b-form-select
                  v-model="filtros.raza"
                  :options="raza(mascotas)"
                  class="mb-3"
                ></b-form-select>
              </div>
            </div>
            <div class="row" v-if="vFiltro">
              <div
                role="button"
                class="bt-hover col-md-1 align-middle text-center"
              >
                <b-icon
                  font-scale="1.5"
                  v-show="filtros.edad != -1"
                  role="button"
                  class="mx-auto btn-outline-danger align-middle"
                  @click="resetEdad"
                  icon="x-square"
                  aria-hidden="true"
                ></b-icon>
              </div>
              <div class="col-md-5">
                <h5>
                  <span
                    class="badge badge-secondary align-middle text-center font-weight-bold shadow-sm p-1"
                    >Edad(Años)</span
                  >
                </h5>
              </div>
              <div class="col-md-5">
                <b-form-select
                  v-model="filtros.edad"
                  :options="edad(mascotas)"
                  class="mb-3"
                ></b-form-select>
              </div>
            </div>
            <div class="row" v-if="vFiltro">
              <div
                role="button"
                class="bt-hover col-md-1 align-middle text-center"
              >
                <b-icon
                  font-scale="1.5"
                  v-show="filtros.sexo != ''"
                  role="button"
                  class="mx-auto btn-outline-danger align-middle"
                  @click="resetSexo"
                  icon="x-square"
                  aria-hidden="true"
                ></b-icon>
              </div>
              <div class="col-md-5">
                <h5>
                  <span
                    class="badge badge-secondary align-middle text-center font-weight-bold shadow-sm p-1"
                    >Sexo</span
                  >
                </h5>
              </div>
              <div class="col-md-5">
                <b-form-select
                  v-model="filtros.sexo"
                  :options="sexo(mascotas)"
                  class="mb-3"
                ></b-form-select>
              </div>
            </div>
            <div class="text-right">
              <b-button
                v-if="vFiltro"
                class="text-right"
                pill
                variant="outline-danger"
                @click="resetFiltros"
                class="my-2"
                ><b-icon icon="trash-fill" aria-hidden="true"></b-icon>
                Filtros</b-button
              >
            </div>
          </div>
        </div>
        <div
          style="background-color: rgba(247, 247, 247, 0.5)!important;"
          class="col-md-7 my-4 shadow bg-light rounded"
        >
          <div v-if="error" class="error">
            {{ error }}
          </div>

          <div v-if="loading" class="d-flex justify-content-center mb-3">
            <b-spinner
              lstyle="width: 3rem; height: 3rem;"
              label="Large Spinner"
            ></b-spinner>
          </div>

          <b-container v-if="!loading" fluid class="p-4">
            <h1 class="my-4">Mascotas en la Comunidad</h1>
            <hr width="90%" />
            <b-row>
              <b-col
                class="mb-4 px-1"
                cols="12"
                sm="6"
                md="4"
                v-for="mascota in paginador(mascotas)"
              >
                <div
                  class="card card-profile text-center rounded-lg shadow w-100 animate__animated animate__fadeIn"
                >
                  <img class="card-img-top" src="@/assets/fondo-profile.jpg" />
                  <div class="card-block">
                    <b-img
                      v-b-modal.modal-center
                      @click="sendInfo(mascota)"
                      class="img-hover card-img-profile"
                      fluid
                      v-bind="mainProps"
                      rounded="circle"
                      :src="mascota.foto"
                      alt="Circle image"
                    ></b-img>
                    <b-col cols="12">
                      <b-icon
                        class="card-text"
                        icon="calendar-date"
                        aria-hidden="true"
                      ></b-icon>
                      <small class="text-muted"
                        >Rescatado: {{ mascota.fecha_rescate }}</small
                      >
                    </b-col>
                    <div class="row">
                      <b-col class="p-0 pl-2" cols="12" lg="4">
                        <b-icon
                          class="card-text"
                          icon="clock-history"
                          aria-hidden="true"
                        ></b-icon>
                        <br /><small class="text-muted"
                          >{{ mascota.edad_aproximada }} Años</small
                        >
                      </b-col>
                      <b-col class="p-0" cols="12" lg="4">
                        <svg width="18" height="18" viewBox="0 0 24 24">
                          <path
                            d="M16 0v2h2.586l-2.113 2.113c-.981-.698-2.177-1.113-3.473-1.113-2.22 0-4.144 1.216-5.18 3.009-3.229.096-5.82 2.738-5.82 5.991 0 2.973 2.164 5.433 5 5.91v2.09h-3v2h3v2h2v-2h3v-2h-3v-2.09c1.791-.301 3.294-1.403 4.167-2.918 3.235-.09 5.833-2.735 5.833-5.992 0-1.296-.415-2.492-1.113-3.473l2.113-2.113v2.586h2v-6h-6zm-3 13c-1.944 0-3.564-1.396-3.923-3.236-.66-.333-1.365-.346-2.033-.066.266 2.293 1.827 4.181 3.931 4.938-.729.831-1.784 1.364-2.975 1.364-2.206 0-4-1.794-4-4s1.794-4 4-4c1.937 0 3.555 1.384 3.921 3.214.679.35 1.309.383 2.033.077-.27-2.293-1.837-4.179-3.943-4.931.732-.83 1.797-1.36 2.989-1.36 2.206 0 4 1.794 4 4s-1.794 4-4 4z"
                          />
                        </svg>
                        <br /><small class="text-muted">
                          {{ mascota.sexo | capitalize }}</small
                        >
                      </b-col>
                      <b-col class="p-0 pr-2" cols="12" lg="4">
                        <router-link
                          class="text-muted"
                          :to="{
                            name: 'Solicitud',
                            params: { tipo: 'Adoptante', mascotaId: mascota.id }
                          }"
                        >
                          <b-icon
                            role="button"
                            class="btn-outline-primary"
                            animation="throb"
                            icon="bookmark-plus"
                            aria-hidden="true"
                          ></b-icon>
                        </router-link>
                        <br /><small class="text-muted">Adoptar</small>
                      </b-col>
                    </div>
                    <div class="card-footer">
                      <h6
                        v-if="mascota.persona"
                        class="text-muted font-weight-bold"
                      >
                        ADOPTADO
                      </h6>
                      <h6 v-else>
                        {{ mascota.nombre }}
                        <b-badge
                          role="button"
                          v-b-modal.modal-center
                          @click="sendInfo(mascota)"
                          >Ver</b-badge
                        >
                      </h6>
                    </div>
                  </div>
                </div>
              </b-col>
              <b-modal
                id="modal-center"
                size="lg"
                class="bg-light"
                centered
                title="BootstrapVue"
              >
                <template v-slot:modal-header="{ close }">
                  <!-- Emulate built in modal header close button action -->
                  <b-button size="sm" variant="outline-danger" @click="close()">
                    Cerrar
                  </b-button>
                  <h4>{{ selectedItem.nombre }}</h4>
                </template>

                <div class="row">
                  <div class="col-md-5 col-sm-12">
                    <b-img
                      class="modal-img-profile"
                      fluid
                      v-bind="mainProps"
                      rounded="circle"
                      :src="selectedItem.foto"
                      alt="Circle image"
                    ></b-img>
                  </div>
                  <div class="col-md-7 col-sm-12">
                    <div class="row my-3">
                      <div class="container text-center">
                        <p class="text-muted">
                          <b-icon
                            class="card-text"
                            icon="calendar-date"
                            aria-hidden="true"
                          ></b-icon>
                          Rescatado: {{ selectedItem.fecha_rescate }} |
                          <b-icon
                            class="card-text"
                            icon="clock-history"
                            aria-hidden="true"
                          ></b-icon>
                          {{ selectedItem.edad_aproximada }} Años |
                          <svg width="18" height="18" viewBox="0 0 24 24">
                            <path
                              d="M16 0v2h2.586l-2.113 2.113c-.981-.698-2.177-1.113-3.473-1.113-2.22 0-4.144 1.216-5.18 3.009-3.229.096-5.82 2.738-5.82 5.991 0 2.973 2.164 5.433 5 5.91v2.09h-3v2h3v2h2v-2h3v-2h-3v-2.09c1.791-.301 3.294-1.403 4.167-2.918 3.235-.09 5.833-2.735 5.833-5.992 0-1.296-.415-2.492-1.113-3.473l2.113-2.113v2.586h2v-6h-6zm-3 13c-1.944 0-3.564-1.396-3.923-3.236-.66-.333-1.365-.346-2.033-.066.266 2.293 1.827 4.181 3.931 4.938-.729.831-1.784 1.364-2.975 1.364-2.206 0-4-1.794-4-4s1.794-4 4-4c1.937 0 3.555 1.384 3.921 3.214.679.35 1.309.383 2.033.077-.27-2.293-1.837-4.179-3.943-4.931.732-.83 1.797-1.36 2.989-1.36 2.206 0 4 1.794 4 4s-1.794 4-4 4z"
                            />
                          </svg>
                          {{ selectedItem.sexo | capitalize }}
                        </p>
                        <p class="text-muted">
                          Especie:
                          <b-badge>{{ selectedItem.especie }}</b-badge> | Raza:
                          <b-badge>{{ selectedItem.raza }}</b-badge>
                        </p>
                      </div>
                    </div>
                    <hr width="90%" />
                    <div class="row my-3">
                      <div class="container">
                        <h5>
                          Sobre <strong>{{ selectedItem.nombre }}</strong
                          >:
                        </h5>
                        <br />
                        <p class="text-justify">
                          {{ selectedItem.reseña }}
                        </p>
                      </div>
                    </div>
                  </div>
                </div>

                <template v-slot:modal-footer="{ hide }">
                  <router-link
                    v-if="!selectedItem.persona"
                    :to="{
                      name: 'Solicitud',
                      params: { tipo: 'Adoptante', mascotaId: selectedItem.id }
                    }"
                    class="btn btn-info"
                    >Adoptar</router-link
                  >
                  <b-button v-else size="sm" variant="info" disabled
                    >Adoptar</b-button
                  >
                </template>
              </b-modal>
            </b-row>

            <div class="mt-3">
              <b-pagination
                align="center"
                v-model="page"
                :per-page="perPage"
                pills
                :total-rows="rows"
              ></b-pagination>
            </div>
          </b-container>
        </div>
      </div>
    </div>

    <div></div>
  </div>
</template>

<script>
import { myMixins } from "@/mixins.js";
import axios from "axios";

export default {
  data() {
    return {
      mascotas: [],
      listado4: [],
      categoria: [],
      options: {
        options1: [],
        options2: [],
        options3: [],
        options4: []
      },
      vFiltro: false,
      filtros: {
        especie: "",
        raza: "",
        edad: -1,
        sexo: "",
        disp: false
      },
      page: 1,
      perPage: 9,
      rows: 0,
      loading: true,
      error: null,
      selectedItem: []
    };
  },
  watch: {
    // call again the method if the route changes
    $route: "getMascotas"
  },
  filters: {
    capitalize: function(value) {
      if (!value) return "";
      value = value.toString();
      return value.charAt(0).toUpperCase() + value.slice(1);
    }
  },
  mixins: [myMixins],
  methods: {
    searchCategoria (id) {
      let auxCat = null
      for (let i=0; i < id.length; i++) {
        auxCat = this.categoria.find(
            element => element.id === id[i]
          );
      }
      return auxCat
    },
    sendInfo(item) {
      this.selectedItem = item;

      let auxCat = this.searchCategoria(this.selectedItem.categoria)

      this.selectedItem.especie = auxCat.especie
      this.selectedItem.raza = auxCat.raza
    },
    getOptions() {
      this.vFiltro = true;
      let auxCat = null
      // Recolección de Options
      for (let i = 0; i < this.mascotas.length; i++) {
        auxCat = this.searchCategoria(this.mascotas[i].categoria)
        this.options.options1[i] = {
          value: auxCat.especie,
          text: auxCat.especie
        };
        this.options.options2[i] = {
          value: auxCat.raza,
          text: auxCat.raza
        };
        this.options.options3[i] = {
          value: this.mascotas[i].edad_aproximada,
          text: this.mascotas[i].edad_aproximada
        };
        this.options.options4[i] = {
          value: this.mascotas[i].sexo,
          text: this.mascotas[i].sexo
        };
      }

      // Options1 (Especie)
      this.options.options1 = this.filtroNuloRepetido(this.options.options1);

      // Options2 (Raza)
      this.options.options2 = this.filtroNuloRepetido(this.options.options2);

      // Options3 (Edad)
      this.options.options3 = this.filtroNuloRepetido(this.options.options3);

      // Options4 (Sexo)
      this.options.options4 = this.filtroNuloRepetido(this.options.options4);
    },

    filtEspecie(filtrados) {
      if (this.filtros.especie != "") {
        let aux = [];
        let auxCat = null
        for (let i = 0; i < filtrados.length; i++) {
          auxCat = this.searchCategoria(filtrados[i].categoria)
          if (
            auxCat.especie ==
            this.filtros.especie
          ) {
            aux[i] = filtrados[i];
          }
        }
        if (aux != []) {
          filtrados = aux;
        }

        filtrados = this.filtroNuloRepetido(filtrados);
      }
      return filtrados;
    },

    filtRaza(filtrados) {
      if (this.filtros.raza != "") {
        let aux = [];
        let auxCat = null
        for (let i = 0; i < filtrados.length; i++) {
          auxCat = this.searchCategoria(filtrados[i].categoria)
          if (
            auxCat.raza == this.filtros.raza
          ) {
            aux[i] = filtrados[i];
          }
        }
        if (aux != []) {
          filtrados = aux;
        }

        filtrados = this.filtroNuloRepetido(filtrados);
      }
      return filtrados;
    },
    filtEdad(filtrados) {
      if (this.filtros.edad != -1) {
        let op = [];
        let aux = [];
        for (let i = 0; i < filtrados.length; i++) {
          if (filtrados[i].edad_aproximada == this.filtros.edad) {
            aux[i] = filtrados[i];
          }
        }
        if (aux != []) {
          filtrados = aux;
        }

        filtrados = this.filtroNuloRepetido(filtrados);
      }
      return filtrados;
    },
    filtSexo(filtrados) {
      if (this.filtros.sexo != "") {
        let aux = [];
        for (let i = 0; i < filtrados.length; i++) {
          if (filtrados[i].sexo == this.filtros.sexo) {
            aux[i] = filtrados[i];
          }
        }
        if (aux != []) {
          filtrados = aux;
        }

        filtrados = this.filtroNuloRepetido(filtrados);
      }
      return filtrados;
    },

    edad(mascotas) {
      let filtrados = [];
      for (let i = 0; i < mascotas.length; i++) {
        filtrados[i] = mascotas[i];
      }

      filtrados = this.filtEspecie(filtrados);
      filtrados = this.filtEspecie(filtrados);
      filtrados = this.filtRaza(filtrados);
      filtrados = this.filtDisp(filtrados);

      //Filtrado de Options
      let op = [];
      for (let i = 0; i < filtrados.length; i++) {
        op[i] = {
          value: filtrados[i].edad_aproximada,
          text: filtrados[i].edad_aproximada
        };
      }

      op = this.filtroNuloRepetido(op);

      let aux3 = [];
      if (
        this.filtros.especie != "" ||
        this.filtros.raza != "" ||
        this.filtros.sexo != ""
      ) {
        aux3 = op;
      } else {
        aux3 = this.options.options3;
      }

      return aux3;
    },
    sexo(mascotas) {
      let filtrados = [];
      for (let i = 0; i < mascotas.length; i++) {
        filtrados[i] = mascotas[i];
      }

      filtrados = this.filtEspecie(filtrados);
      filtrados = this.filtRaza(filtrados);
      filtrados = this.filtEdad(filtrados);
      filtrados = this.filtDisp(filtrados);

      //Filtrado de Options
      let op = [];
      for (let i = 0; i < filtrados.length; i++) {
        op[i] = { value: filtrados[i].sexo, text: filtrados[i].sexo };
      }

      op = this.filtroNuloRepetido(op);

      let aux3 = [];
      if (
        this.filtros.especie != "" ||
        this.filtros.raza != "" ||
        this.filtros.edad != -1
      ) {
        aux3 = op;
      } else {
        aux3 = this.options.options4;
      }

      return aux3;
    },
    especie(mascotas) {
      let filtrados = [];
      for (let i = 0; i < mascotas.length; i++) {
        filtrados[i] = mascotas[i];
      }

      filtrados = this.filtRaza(filtrados);
      filtrados = this.filtEdad(filtrados);
      filtrados = this.filtSexo(filtrados);
      filtrados = this.filtDisp(filtrados);

      //Filtrado de Options
      let op = [];
      let auxCat = null
      for (let i = 0; i < filtrados.length; i++) {
        auxCat = this.searchCategoria(filtrados[i].categoria)
        op[i] = {
          value: auxCat.especie,
          text: auxCat.especie
        };
      }
      op = this.filtroNuloRepetido(op);

      let aux3 = [];
      if (
        this.filtros.raza != "" ||
        this.filtros.sexo != "" ||
        this.filtros.edad != -1
      ) {
        aux3 = op;
      } else {
        aux3 = this.options.options1;
      }

      return aux3;
    },
    raza(mascotas) {
      let filtrados = [];
      for (let i = 0; i < mascotas.length; i++) {
        filtrados[i] = mascotas[i];
      }

      filtrados = this.filtEspecie(filtrados);
      filtrados = this.filtEdad(filtrados);
      filtrados = this.filtSexo(filtrados);
      filtrados = this.filtDisp(filtrados);

      //Filtrado de Options
      let op = [];
      let auxCat = null
      for (let i = 0; i < filtrados.length; i++) {
        auxCat = this.searchCategoria(filtrados[i].categoria)
        op[i] = {
          value: auxCat.raza,
          text: auxCat.raza
        };
      }

      op = this.filtroNuloRepetido(op);

      let aux3 = [];
      if (
        this.filtros.especie != "" ||
        this.filtros.sexo != "" ||
        this.filtros.edad != -1
      ) {
        aux3 = op;
      } else {
        aux3 = this.options.options2;
      }

      return aux3;
    },
    paginador(mascotas) {
      let filtrados = [];
      for (let i = 0; i < mascotas.length; i++) {
        filtrados[i] = mascotas[i];
      }

      filtrados = this.filtEspecie(filtrados);
      filtrados = this.filtRaza(filtrados);
      filtrados = this.filtEdad(filtrados);
      filtrados = this.filtSexo(filtrados);
      filtrados = this.filtDisp(filtrados);

      this.rows = filtrados.length;

      const indiceInicio = (this.page - 1) * this.perPage;
      const indiceFinal =
        indiceInicio + this.perPage > filtrados.length
          ? filtrados.length
          : indiceInicio + this.perPage;
      return filtrados.slice(indiceInicio, indiceFinal);
    },
    resetFiltros() {
      this.filtros.especie = "";
      this.filtros.raza = "";
      this.filtros.edad = -1;
      this.filtros.sexo = "";
      this.filtros.disp = false;
    },
    resetEspecie() {
      this.filtros.especie = "";
    },
    resetRaza() {
      this.filtros.raza = "";
    },
    resetEdad() {
      this.filtros.edad = -1;
    },
    resetSexo() {
      this.filtros.sexo = "";
    },
    resetDisp() {
      this.filtros.disp = false;
    }
  },
  created() {
    this.scrollBehavior(), this.getMascotas(), this.getCategoria();
  }
};
</script>

<style scoped>
.bt-hover:hover {
  transition-property: transform;
  transition-duration: 0.2s;
  -webkit-transform: scale(1.3);
  -ms-transform: scale(1.3);
  transform: scale(1.3);
}
.img-hover:hover {
  transition-property: transform;
  transition-duration: 0.2s;
  -webkit-transform: scale(1.8);
  -ms-transform: scale(1.8);
  transform: scale(1.8);
  position: relative;
  z-index: 10;
  cursor: pointer;
}
.card-profile {
  background-color: #f7f7f7;
}
.card-profile .card-img-top {
  border-radius: 0;
}
.card-profile .card-img-profile {
  max-width: 70%;
  margin-top: -40px;
  border: 5px solid #f7f7f7;
}
.modal-img-profile {
  border: 5px solid #f7f7f7;
  max-height: 300px;
  height: 100%;
  width: 100%;
  display: block;
  object-fit: cover;
  object-position: center center;
}
.card-img-top {
  max-width: 100%;
  max-height: 80px;
}
</style>
