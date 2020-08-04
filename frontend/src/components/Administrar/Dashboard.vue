<template>
    <div class="container">
        <div class="row">
        <div class="col-md-8 col-sm-12 bg-light rounded-lg shadow my-4">
          <h1 class="my-4">
            Dashboard Administración
          </h1>
          <hr width="90%" />

          <!-- Notificaciones -->
          <div>
            <h3>Notificaciones <b-badge v-if="notificaciones(items)>0" pill variant="danger">{{ counter }}</b-badge></h3>
            <hr width="90%" />
            <h5>Pre Solicitudes</h5>
            <br>

            <b-row>
                <b-col lg="6" class="my-1">
                    <b-form-group
                    label="Filtrar"
                    label-cols-sm="3"
                    label-align-sm="right"
                    label-size="sm"
                    label-for="filterInput"
                    class="mb-0"
                    >
                    <b-input-group size="sm">
                        <b-form-input
                        v-model="filter"
                        type="search"
                        id="filterInput"
                        placeholder="escribe para buscar"
                        ></b-form-input>
                        <b-input-group-append>
                        <b-button :disabled="!filter" @click="filter = ''">Limpiar</b-button>
                        </b-input-group-append>
                    </b-input-group>
                    </b-form-group>
                </b-col>

                <b-col sm="5" md="6" class="my-1">
                    <b-form-group
                    label="Por página"
                    label-cols-sm="6"
                    label-cols-md="4"
                    label-cols-lg="3"
                    label-align-sm="right"
                    label-size="sm"
                    label-for="perPageSelect"
                    class="mb-0"
                    >
                    <b-form-select
                        v-model="perPage"
                        id="perPageSelect"
                        size="sm"
                        :options="pageOptions"
                    ></b-form-select>
                    </b-form-group>
                </b-col>

                <b-col sm="12" md="12" class="my-1">
                    <b-pagination
                    v-model="currentPage"
                    :total-rows="totalRows"
                    :per-page="perPage"
                    align="center"
                    size="sm"
                    class="my-2"
                    pills
                    ></b-pagination>
                </b-col>
            </b-row>

                <!-- Main table element -->
                <b-table
                show-empty
                small
                stacked="md"
                :items="items"
                :fields="fields"
                :current-page="currentPage"
                :per-page="perPage"
                :filter="filter"
                @filtered="onFiltered"
                table-variant="light"
                head-variant="dark"
                hover
                >

                <template v-slot:cell(check)="row">
                    <b-icon v-if="!row.value" icon="circle-fill" variant="danger"></b-icon>
                    <b-icon v-else icon="check-all" variant="success"></b-icon>
                    <div v-if="row.item.foto">
                      <img id="addImg" v-show="false" :src="row.item.foto" alt="">
                    </div>
                </template>

                <template v-slot:cell(config)="row">
                    <router-link :to="{ name: 'preSolicitud', params: { preSolicitudId: row.item.id } }"><b-icon role="button" variant="dark" icon="tools" v-b-tooltip.hover title="Gestionar Solicitud"></b-icon></router-link>
                </template>
            </b-table>

            <hr width="90%" />

            <h5>Solicitudes Aprobadas</h5>
            <br>

            <b-row>
                <b-col lg="6" class="my-1">
                    <b-form-group
                    label="Filtrar"
                    label-cols-sm="3"
                    label-align-sm="right"
                    label-size="sm"
                    label-for="filterInput2"
                    class="mb-0"
                    >
                    <b-input-group size="sm">
                        <b-form-input
                        v-model="filter2"
                        type="search"
                        id="filterInput2"
                        placeholder="escribe para buscar"
                        ></b-form-input>
                        <b-input-group-append>
                        <b-button :disabled="!filter2" @click="filter2 = ''">Limpiar</b-button>
                        </b-input-group-append>
                    </b-input-group>
                    </b-form-group>
                </b-col>

                <b-col sm="5" md="6" class="my-1">
                    <b-form-group
                    label="Por página"
                    label-cols-sm="6"
                    label-cols-md="4"
                    label-cols-lg="3"
                    label-align-sm="right"
                    label-size="sm"
                    label-for="perPageSelect2"
                    class="mb-0"
                    >
                    <b-form-select
                        v-model="perPage2"
                        id="perPageSelect2"
                        size="sm"
                        :options="pageOptions"
                    ></b-form-select>
                    </b-form-group>
                </b-col>

                <b-col sm="12" md="12" class="my-1">
                    <b-pagination
                    v-model="currentPage2"
                    :total-rows="totalRows2"
                    :per-page="perPage2"
                    align="center"
                    size="sm"
                    class="my-2"
                    pills
                    ></b-pagination>
                </b-col>
            </b-row>

                <!-- Main table element -->
                <b-table
                show-empty
                small
                stacked="md"
                :items="items2"
                :fields="fields2"
                :current-page="currentPage2"
                :per-page="perPage2"
                :filter="filter2"
                @filtered="onFiltered2"
                table-variant="light"
                head-variant="dark"
                hover
                >

                <template v-slot:cell(persona)="row">
                  <a :href="'/api/v1.0/adopcion/personas/'+searchPersona(row.value, personas).id">{{ searchPersona(row.value, personas).nombre }} {{ searchPersona(row.value, personas).apellidos }}</a>
                </template>

                <template v-slot:cell(mascotas)="row">
                  <a v-for="(id, index) in row.value" :key="index" :href="'/api/v1.0/mascota/all/'+id">{{ id }}</a>
                </template>

            </b-table>

          </div>
          <!-- /Notificaciones -->
        </div>

        <div class="col-md-4 col-sm-12 animate__animated animate__backInRight">
          <div class="col-md-12 mt-4 mb-2 mr-3 py-3 shadow bg-light rounded">
            <h2 class="font-italic">Sub Panel</h2>
          </div>

          <b-card
            title="Categorias"
            class="bg-opaco mb-2 border-0 shadow"
            sub-title="en Admin"
          >
            <b-card-text>
              <div class="row">
                <div class="col-md-6">
                  <p><a href="/admin/mascota/mascota/"><small>Mascotas</small></a></p>
                  <p><a href="/admin/adopcion/persona/"><small>Personas</small></a></p>
                  <p><a href="/admin/mascota/vacuna/"><small>Vacunas</small></a></p>
                </div>
                <div class="col-md-6">
                  <p><a href="/admin/noticias/noticia/"><small>Noticias</small></a></p>
                  <p><a href="/admin/adopcion/solicitud/"><small>Solicitudes</small></a></p>
                  <p><a href="/admin/auth/user/"><small>Usuarios</small></a></p>
                </div>
              </div>
            </b-card-text>
          </b-card>
        </div>
      </div>
    </div>
</template>

<script>
import { myMixins } from "@/mixins.js";

  export default {
    name: "Dashboard",
    data() {
      return {
        counter: 0,
        pageOptions: [5, 10, 15],
        filter: null,
        filter2: null,
        totalRows: 1,
        totalRows2: 1,
        currentPage: 1,
        currentPage2: 1,
        perPage: 5,
        perPage2: 5,
        fields: [
          { key: 'id', sortable: true },
          { key: 'tipo', sortable: true },
          { key: 'nombre', sortable: true },
          { key: 'aprobar', sortable: true },
          { key: 'check', label: 'Check', sortable: true },
          { key: 'config', label: 'Gestión' }
        ],
        fields2: [
          { key: 'id', sortable: true },
          { key: 'tipo', sortable: true },
          { key: 'persona', sortable: true },
          { key: 'mascotas', sortable: true }
        ],
        items: [],
        items2: [],
        personas: []
      }
    },
    mixins: [myMixins],
    methods: {
        onFiltered(filteredItems) {
        // Trigger pagination to update the number of buttons/pages due to filtering
        this.totalRows = filteredItems.length
        this.currentPage = 1
        },
        onFiltered2(filteredItems) {
        // Trigger pagination to update the number of buttons/pages due to filtering
        this.totalRows2 = filteredItems.length
        this.currentPage2 = 1
        },
        searchPersona(id, personas) {
          let aux = personas.find(
            element => element.id === id
          );

          return aux
        },
        notificaciones(items) {
          let aux = 0
            for (let i=0; i<items.length; i++) {
                if (!items[i].check) {
                    aux++
                    this.items[i]._rowVariant = 'danger'
                } else {
                    this.items[i]._rowVariant = ''
                }
            }
            this.counter = aux
            return aux
        }
    },
    created() {
      this.scrollBehavior(),
      this.getPreSolicitud(),
      this.getSolicitud(),
      this.getPersonas()
    },
    beforeUpdate() {
      this.getPreSolicitud(),
      this.getSolicitud(),
      this.getPersonas()
    }
  }
</script>