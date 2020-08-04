<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-md-8 col-sm-12 bg-light rounded-lg shadow my-4">
          <h1 class="my-4">Solicitud a <small>Casa Adoptiva</small></h1>
          <hr width="90%" />

          <b-form @submit="onSubmit" class="mb-3">
            <div v-show="show">
              <h3 class="my-2">Datos de la Persona</h3>
              <hr width="90%" />

              <b-form-group
                id="input-group-tipo"
                label="Tipo de Solicitud:"
                label-for="input-tipo"
              >
                <b-form-select
                  v-if="!$route.params.tipo"
                  id="input-tipo"
                  v-model="form.tipo"
                  required
                >
                  <b-form-select-option :value="null"
                    >Por favor seleccione una opción</b-form-select-option
                  >
                  <b-form-select-option value="Padrino"
                    >Padrino</b-form-select-option
                  >
                  <b-form-select-option value="Adoptante"
                    >Adoptante</b-form-select-option
                  >
                </b-form-select>
                <b-form-select
                  v-else
                  id="input-tipo"
                  v-model="form.tipo"
                  required
                >
                  <b-form-select-option :value="$route.params.tipo">{{
                    $route.params.tipo
                  }}</b-form-select-option>
                </b-form-select>
              </b-form-group>

              <b-form-group
                id="input-group-0"
                label="Tu telefono:"
                label-for="input-0"
              >
                <b-form-input
                  id="input-0"
                  v-model="form.telefono"
                  required
                  placeholder="Ingrese su N° de telefono"
                ></b-form-input>
              </b-form-group>

              <b-form-group
                id="input-group-1"
                label="Email:"
                label-for="input-1"
                description="Nunca compartiremos su correo electrónico con nadie más."
              >
                <b-form-input
                  id="input-1"
                  v-model="form.email"
                  type="email"
                  required
                  placeholder="Ingrese email"
                ></b-form-input>
              </b-form-group>

              <b-form-group
                id="input-group-2"
                label="Tu Nombre:"
                label-for="input-2"
              >
                <b-form-input
                  id="input-2"
                  v-model="form.nombre"
                  required
                  placeholder="Ingrese su nombre"
                ></b-form-input>
              </b-form-group>

              <b-form-group
                id="input-group-3"
                label="Tus Apellidos:"
                label-for="input-3"
              >
                <b-form-input
                  id="input-3"
                  v-model="form.apellidos"
                  required
                  placeholder="Ingrese su apellido"
                ></b-form-input>
              </b-form-group>

              <b-form-group
                id="input-group-4"
                label="Tu Edad:"
                label-for="input-4"
              >
                <b-form-input
                  id="input-4"
                  v-model="form.edad"
                  required
                  placeholder="Ingrese su edad en años"
                  type="number"
                ></b-form-input>
              </b-form-group>

              <b-form-group
                id="input-group-5"
                label="Tu Domicilio:"
                label-for="input-5"
              >
                <b-form-textarea
                  id="input-5"
                  v-model="form.domicilio"
                  required
                  placeholder="Ingrese la dirección de su domicilio"
                  rows="2"
                  max-rows="3"
                ></b-form-textarea>
              </b-form-group>

              <b-form-group
                id="input-group-6"
                label="N° de Mascotas:"
                label-for="input-6"
              >
                <b-form-input
                  id="input-6"
                  v-model="form.numero_mascotas"
                  required
                  placeholder="Ingrese cantidad de mascotas"
                  type="number"
                ></b-form-input>
              </b-form-group>

              <b-form-group
                id="input-group-7"
                label="Razones:"
                label-for="input-7"
              >
                <b-form-textarea
                  id="input-7"
                  v-model="form.razones"
                  placeholder="Ingrese el mensaje..."
                  rows="3"
                  max-rows="6"
                ></b-form-textarea>
              </b-form-group>

              <b-button class="mx-1" @click="mascotaExist" variant="info"
                >Siguiente</b-button
              >
            </div>

            <div v-show="!show">
              <h3 class="my-2">Datos de la Mascota</h3>
              <hr width="90%" />

              <div v-if="form.tipo == 'Padrino'">
                <b-form-group
                  id="input-group-8"
                  label="Nombre:"
                  label-for="input-8"
                >
                  <b-form-input
                    id="input-8"
                    v-model="form.nombre_mascota"
                    required
                    placeholder="Ingrese nombre de la mascota"
                  ></b-form-input>
                </b-form-group>

                <b-form-group
                  id="input-group-9"
                  label="Sexo:"
                  label-for="input-9"
                >
                  <b-form-select id="input-9" v-model="form.sexo" required>
                    <b-form-select-option :value="null"
                      >Por favor seleccione una opción</b-form-select-option
                    >
                    <b-form-select-option value="Hembra"
                      >Hembra</b-form-select-option
                    >
                    <b-form-select-option value="Macho"
                      >Macho</b-form-select-option
                    >
                  </b-form-select>
                </b-form-group>

                <b-form-group
                  id="input-group-10"
                  label="Edad aproximada:"
                  label-for="input-10"
                >
                  <b-form-input
                    id="input-10"
                    v-model="form.edad_aproximada"
                    required
                    placeholder="Ingrese edad en años"
                    type="number"
                  ></b-form-input>
                </b-form-group>

                <b-form-group
                  id="input-group-11"
                  label="Fecha de rescate:"
                  label-for="input-11"
                >
                  <b-form-datepicker
                    id="input-11"
                    v-model="form.fecha_rescate"
                    required
                  ></b-form-datepicker>
                </b-form-group>

                <b-form-group
                  id="input-group-12"
                  label="Vacunas:"
                  label-for="input-12"
                >
                  <b-form-checkbox-group
                    id="input-12"
                    v-model="form.vacuna"
                    :options="vacunas"
                    name="flavour-1"
                  ></b-form-checkbox-group>
                </b-form-group>

                <b-form-group
                  id="input-group-13"
                  label="Foto:"
                  label-for="input-13"
                >
                  <b-form-file
                    id="input-13"
                    v-model="foto"
                    :state="Boolean(foto)"
                    accept="image/*"
                    placeholder="Elija un archivo o suéltelo aquí..."
                    drop-placeholder="Suelta el archivo aquí..."
                  ></b-form-file>
                </b-form-group>

                <b-form-group
                  id="input-group-14"
                  label="Especie:"
                  label-for="input-14"
                >
                  <b-form-input
                    id="input-14"
                    v-model="form.especie"
                    placeholder="Ejemplo: Perro, Gato, Otros..."
                    required
                  ></b-form-input>
                </b-form-group>

                <b-form-group
                  id="input-group-15"
                  label="Raza:"
                  label-for="input-15"
                >
                  <b-form-input
                    id="input-15"
                    v-model="form.raza"
                    placeholder="Ejemplo: Dalmata, Montañez, Otros..."
                    required
                  ></b-form-input>
                </b-form-group>

                <b-form-group
                  id="input-group-16"
                  label="Reseña:"
                  label-for="input-16"
                >
                  <b-form-input
                    id="input-16"
                    v-model="form.reseña"
                    placeholder="Descripción de la mascota..."
                    required
                  ></b-form-input>
                </b-form-group>
              </div>

              <div v-else>
                <a
                  @click="$bvModal.show('modal-search')"
                  class="btn btn-secondary text-light"
                  >Buscar Mascota / Cambiar Mascota</a
                >
                <hr width="90%" />
                <a
                  v-if="form.mascota.id"
                  v-b-modal.modal-select
                  class="btn btn-secondary text-light"
                  >Datos de la Mascota: {{ form.mascota.nombre }}</a
                >
                <p v-else class="text-muted">Debe seleccionar una mascota!</p>
                <hr width="90%" />
              </div>

              <b-modal
                id="modal-search"
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
                  <h4>Seleccione Mascota</h4>
                </template>
                <div class="row">
                  <div class="col-md-12 text-center">
                    <b-input-group class="mt-3">
                      <b-form-input
                        v-model="searchText"
                        placeholder="Buscar mascota..."
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
                  </div>
                </div>
                <hr width="90%" />
                <div class="row">
                  <div
                    v-for="(mascota, index) in paginador(searchFilt(mascotas))"
                    :key="index"
                    class="col-md-4 col-sm-6 text-center"
                  >
                    <b-img
                      class="modal-img-search"
                      fluid
                      rounded="circle"
                      :src="mascota.foto"
                      alt="Circle image"
                    ></b-img>
                    <h6>{{ mascota.nombre }}</h6>
                    <button
                      class="btn btn-outline-success"
                      @click="seleccion(mascota)"
                    >
                      Seleccionar
                    </button>
                  </div>
                </div>
                <hr width="90%" />
                <div class="mt-3">
                  <b-pagination
                    align="center"
                    v-model="page"
                    :per-page="perPage"
                    pills
                    :total-rows="rows"
                  ></b-pagination>
                </div>

                <template v-slot:modal-footer="{ ok }">
                  <button
                    @click="confirmar"
                    class="btn"
                    v-bind:class="{
                      'btn-outline-info': showConfirmar,
                      'btn-info': !showConfirmar
                    }"
                  >
                    Confirmar
                  </button>
                  <b-button @click="ok()" variant="outline-success"
                    >Ok</b-button
                  >
                </template>
              </b-modal>

              <b-modal
                id="modal-select"
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
                  <h4>{{ form.mascota.nombre }}</h4>
                </template>

                <div class="row">
                  <div class="col-md-5 col-sm-12">
                    <b-img
                      class="modal-img-profile"
                      fluid
                      rounded="circle"
                      :src="form.mascota.foto"
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
                          Rescatado: {{ form.mascota.fecha_rescate }} |
                          <b-icon
                            class="card-text"
                            icon="clock-history"
                            aria-hidden="true"
                          ></b-icon>
                          {{ form.mascota.edad_aproximada }} Años |
                          <svg width="18" height="18" viewBox="0 0 24 24">
                            <path
                              d="M16 0v2h2.586l-2.113 2.113c-.981-.698-2.177-1.113-3.473-1.113-2.22 0-4.144 1.216-5.18 3.009-3.229.096-5.82 2.738-5.82 5.991 0 2.973 2.164 5.433 5 5.91v2.09h-3v2h3v2h2v-2h3v-2h-3v-2.09c1.791-.301 3.294-1.403 4.167-2.918 3.235-.09 5.833-2.735 5.833-5.992 0-1.296-.415-2.492-1.113-3.473l2.113-2.113v2.586h2v-6h-6zm-3 13c-1.944 0-3.564-1.396-3.923-3.236-.66-.333-1.365-.346-2.033-.066.266 2.293 1.827 4.181 3.931 4.938-.729.831-1.784 1.364-2.975 1.364-2.206 0-4-1.794-4-4s1.794-4 4-4c1.937 0 3.555 1.384 3.921 3.214.679.35 1.309.383 2.033.077-.27-2.293-1.837-4.179-3.943-4.931.732-.83 1.797-1.36 2.989-1.36 2.206 0 4 1.794 4 4s-1.794 4-4 4z"
                            />
                          </svg>
                          {{ form.mascota.sexo | capitalize }}
                        </p>
                        <p class="text-muted">
                          Especie:
                          <b-badge>{{ form.mascota.especie }}</b-badge> | Raza:
                          <b-badge>{{ form.mascota.raza }}</b-badge>
                        </p>
                      </div>
                    </div>
                    <hr width="90%" />
                    <div class="row my-3">
                      <div class="container">
                        <h5>
                          Sobre <strong>{{ form.mascota.nombre }}</strong
                          >:
                        </h5>
                        <br />
                        <p class="text-justify">
                          {{ form.mascota.reseña }}
                        </p>
                      </div>
                    </div>
                  </div>
                </div>

                <template v-slot:modal-footer>
                  <b-button size="sm" variant="info" disabled>Adoptar</b-button>
                </template>
              </b-modal>

              <b-button class="mx-1" @click="show = !show" variant="secondary"
                >Atras</b-button
              >
              <b-button class="mx-1" type="submit" variant="info"
                >Enviar</b-button
              >
            </div>
          </b-form>
        </div>
        <div class="col-md-4 col-sm-12 animate__animated animate__backInRight">
          <div class="col-md-12 mt-4 mb-2 mr-3 py-3 shadow bg-light rounded">
            <h2 class="font-italic">Solicitud</h2>
          </div>

          <b-card
            title="Buscar"
            class="bg-opaco mb-2 border-0 shadow"
            sub-title="Noticias"
          >
            <b-card-text> </b-card-text>
          </b-card>

          <b-card
            title="Categorias"
            class="bg-opaco mb-2 border-0 shadow"
            sub-title="Más noticias"
          >
            <b-card-text>
              <div class="row"></div>
            </b-card-text>
          </b-card>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { myMixins } from "@/mixins.js";
import axios from "axios";

export default {
  name: "Solicitud",
  data() {
    return {
      form: {
        nombre: "",
        apellidos: "",
        edad: "",
        telefono: "",
        email: "",
        domicilio: "",

        numero_mascotas: "",
        razones: "",
        tipo: "",
        aprobar: "false",
        mascota: [],

        nombre_mascota: "",
        sexo: "",
        edad_aproximada: null,
        fecha_rescate: null,
        vacuna: [],
        // foto: null,
        especie: "",
        raza: "",
        reseña: "default"
      },
      foto: null,
      vacunas: [],
      show: true,
      showConfirmar: true,
      mascotas: [],
      listado4: [],
      page: 1,
      perPage: 6,
      rows: 0,
      seleccionado: {},
      searchText: "",
      filtros: {
        disp: true
      }
    };
  },
  mixins: [myMixins],
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      let id = this.mascotas[0].id;
      if (this.form.mascota.id) {
        id = this.form.mascota.id;
      }
      this.form.mascota = [];
      this.form.mascota.push(id);

      let aux = null;

      if (this.form.tipo == "Padrino") {
        
        aux = this.objToFormData(this.form)

        let imagefile = document.querySelector("#input-13");
        aux.append("foto", imagefile.files[0]);

        const path = "http://localhost:8000/api/v1.0/adopcion/pre-solicitud/";
        axios
          .post(path, aux, {
            headers: {
              "Content-Type": "multipart/form-data"
            }
          })
          .then(response => {
            aux = response.data;
            this.$swal.fire(
              'Solicitud creada exitosamente!',
              'Presiona ok!',
              'success'
            )
          })
          .catch(error => {
            this.$swal.fire({
              icon: 'error',
              title: 'Oops...',
              text: error,
            })
            console.log(error);
          });
      }

      if (this.form.tipo == "Adoptante") {
        aux = this.form;

        const path = "http://localhost:8000/api/v1.0/adopcion/pre-solicitud/";
        axios
          .post(path, aux)
          .then(response => {
            aux = response.data;
            this.$swal.fire(
              'Solicitud creada exitosamente!',
              'Presiona ok!',
              'success'
            )
          })
          .catch(error => {
            this.$swal.fire({
              icon: 'error',
              title: 'Oops...',
              text: error,
            })
            console.log(error);
          });
      }
    },
    mascotaExist() {
      this.show = !this.show;
      if (this.$route.params.mascotaId) {
        this.form.mascota = this.mascotas.find(
          element => element.id === this.$route.params.mascotaId
        );
      }
    },
    seleccion(mascota) {
      this.seleccionado = mascota;
      this.showConfirmar = true;
    },
    confirmar() {
      this.form.mascota = this.seleccionado;
      this.seleccionado = {};
      this.showConfirmar = false;
    },
    paginador(mascotas) {
      let filtrados = [];
      for (let i = 0; i < mascotas.length; i++) {
        filtrados[i] = mascotas[i];
      }

      filtrados = this.filtDisp(filtrados);

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
    this.scrollBehavior(),
    this.getMascotas(), 
    this.getVacunas()
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
.modal-img-search {
  border: 3px solid #f7f7f7;
  width: 100%;
  display: block;
  object-fit: cover;
  object-position: center center;
}
</style>
