<template>
    <div class="container">
        <div class="row">
            <div class="col-md-8 col-sm-12 bg-light rounded-lg shadow my-4">
                <h1 class="my-4">
                    Gestionar Pre-Solicitud N°{{ $route.params.preSolicitudId }}
                </h1>
                <hr width="90%" />

                <h4>Datos de la Persona</h4>
                <b-table
                    show-empty
                    small
                    stacked
                    :items="obtainItem(items)"
                    :fields="fieldsP"
                    table-variant="light"
                    head-variant="dark"
                    hover
                >
                </b-table>
                <hr width="90%" />
                <h4>Datos de la Solicitud</h4>
                <b-table
                    show-empty
                    small
                    stacked
                    :items="obtainItem(items)"
                    :fields="fieldsS"
                    table-variant="light"
                    head-variant="dark"
                    hover
                >
                </b-table>
                <hr width="90%" />
                <h4>Datos de la Mascota</h4>
                <b-table
                    show-empty
                    small
                    stacked
                    :items="obtainM(items, mascotas)"
                    :fields="fieldsM"
                    table-variant="light"
                    head-variant="dark"
                    hover
                >
                    <template v-slot:cell(foto)="row">
                        <div class="square">
                            <b-img
                                id="addImg"
                                class="img-fluid"
                                rounded="circle"
                                :src="row.value"
                                alt="Circle image"
                            ></b-img>
                        </div>
                    </template>

                    <template v-slot:cell(vacuna)="row">
                        <b-badge v-for="(vacuna, index) in row.value" :key="index" class="mx-1" variant="secondary">{{ vacunas[vacuna].text }}</b-badge>
                    </template>

                    <template v-slot:cell(nombre_mascota)="row">
                        <p v-if="row.item.tipo == 'Padrino'">{{ row.value }}</p>
                        <p v-else>{{ row.item.nombre }}</p>
                    </template>
                </b-table>
                <button @click="aprobar(items)" class="btn btn-success">Aprobar</button>
                <hr width="90%" />

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
import axios from 'axios';
import { myMixins } from "@/mixins.js";

  export default {
    name: "PreSolicitud",
    data() {
      return {
        fieldsP: [
          { key: 'nombre' },
          { key: 'apellidos' },
          { key: 'edad' },
          { key: 'telefono' },
          { key: 'email' },
          { key: 'domicilio' }
        ],
        fieldsS: [
          { key: 'tipo' },
          { key: 'numero_mascotas' },
          { key: 'razones' }
        ],
        fieldsM: [
          { key: 'nombre_mascota' },
          { key: 'sexo' },
          { key: 'edad_aproximada' },
          { key: 'fecha_rescate' },
          { key: 'vacuna' },
          { key: 'foto' },
          { key: 'especie' },
          { key: 'raza' },
          { key: 'reseña' }
        ],
        items: [],
        id: this.$route.params.preSolicitudId,
        vacunas: [],
        mascotas: [],
        listado4: [],
        categoria: [],
        mascotaId: null
      }
    },
    mixins: [myMixins],
    methods: {
        obtainItem(items) {
            let aux = []
            for (let i=0; i<items.length; i++) {
                if (this.id == items[i].id) {
                    aux[0] = items[i]
                }
            }
            return aux
        },
        obtainM(items, mascotas) {
            let aux = [
                {tipo: null}
            ]
            let aux2 = []
            for (let i=0; i<items.length; i++) {
                if (this.id == items[i].id) {
                    aux[0] = items[i]
                }
            }
            if (aux[0].tipo == 'Padrino') {
                return aux
            } else {
                for (let i=0; i<mascotas.length; i++) {
                    if (aux[0].mascota == mascotas[i].id) {
                        aux2[0] = mascotas[i]
                        this.mascotaId = mascotas[i].id
                    }
                }
                return aux2
            }
        },
        verificarCategoria(item) {
            let auxCat = { especie: item.especie, raza: item.raza}
            let auxId = null
            for (let i=0; i<this.categoria.length; i++) {
                if (this.categoria[i].especie == auxCat.especie && this.categoria[i].raza == auxCat.raza) {
                    auxId = this.categoria[i].id
                    return auxId
                }
            }

            if (auxId == null) {
                const path = "http://localhost:8000/api/v1.0/mascota/categoria/";
                    axios
                    .post(path, auxCat)
                    .then(response => {
                        auxCat = response.data;
                        auxId = response.data.id
                        this.$swal.fire(
                            'Categoria creada exitosamente!',
                            'Presiona ok!',
                            'success'
                        )
                        return auxId
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
        aprobar(items) {
            let auxP = {}
            let auxM = {}
            let auxS = {}
            let tipo = null
            let personaId = null
            let base64String = null
            let formData2 = new FormData();
            for (let i=0; i<items.length; i++) {
                if (this.id == items[i].id) {
                    tipo = items[i].tipo

                    auxP.nombre = items[i].nombre
                    auxP.apellidos = items[i].apellidos
                    auxP.edad = items[i].edad
                    auxP.telefono = items[i].telefono
                    auxP.email = items[i].email
                    auxP.domicilio = items[i].domicilio

                    auxM.nombre = items[i].nombre_mascota
                    auxM.sexo = items[i].sexo
                    auxM.edad_aproximada = items[i].edad_aproximada
                    auxM.fecha_rescate = items[i].fecha_rescate
                    // auxM.persona = items[i].
                    // auxM.padrino = items[i].
                    auxM.vacuna = items[i].vacuna


                    let c = document.createElement('canvas');
                    let img = document.getElementById('addImg');
                    c.height = img.naturalHeight;
                    c.width = img.naturalWidth;
                    let ctx = c.getContext('2d');

                    ctx.drawImage(img, 0, 0, c.width, c.height);
                    base64String = c.toDataURL('image/jpeg', 0.6);

                    auxM.reseña = items[i].reseña
                    if (items[i].tipo == 'Padrino') {
                        auxM.categoria = this.verificarCategoria(items[i])
                    }
                    // auxS.persona = items[i].
                    auxS.numero_mascotas = items[i].numero_mascotas
                    auxS.razones = items[i].razones
                    auxS.tipo = items[i].tipo
                    auxS.aprobar = 'Si'
                    // auxS.mascotas = items[i].
                }
            }
            
            auxM = this.objToFormData(auxM)

            this.dataURLtoBlob(base64String , function( blob )
            {
                auxM.append("foto", blob, 'mascota.jpg');
                formData2.append("foto", blob, 'mascota.jpg');
            });

            const path = "http://localhost:8000/api/v1.0/adopcion/personas/";
            axios
            .post(path, auxP)
            .then(response => {
                auxP = response.data;
                personaId = response.data.id
                this.$swal.fire(
                    'Persona creada exitosamente!',
                    'Presiona ok!',
                    'success'
                )

                if (tipo == 'Padrino') {
                    auxM.append("padrino", personaId)
                   
                    const path2 = "http://localhost:8000/api/v1.0/mascota/all/";
                    axios
                    .post(path2, auxM)
                    .then(res => {
                        auxM = res.data;
                        this.mascotaId = res.data.id
                        this.$swal.fire(
                            'Mascota creada exitosamente!',
                            'Presiona ok!',
                            'success'
                        )

                        auxS.persona = personaId
                        auxS.mascotas = []
                        auxS.mascotas.push(this.mascotaId)
                        const path3 = "http://localhost:8000/api/v1.0/adopcion/solicitud/";
                            axios
                            .post(path3, auxS)
                            .then(response3 => {
                                auxS = response3.data;
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
                    })
                    .catch(error => {
                        this.$swal.fire({
                            icon: 'error',
                            title: 'Oops...',
                            text: error,
                        })
                        console.log(error);
                    });
                } else {
                   
                    const path2 = 'http://localhost:8000/api/v1.0/mascota/all/' + this.mascotaId + '/';

                    axios
                    .get(path2)
                    .then(response => {
                        let mascotaPut = response.data
                        formData2.append("nombre", mascotaPut.nombre)
                        formData2.append("sexo", mascotaPut.sexo)
                        formData2.append("edad_aproximada", mascotaPut.edad_aproximada)
                        formData2.append("fecha_rescate", mascotaPut.fecha_rescate)
                        formData2.append("reseña", mascotaPut.reseña)
                        formData2.append("persona", personaId)
                        if (mascotaPut.padrino) {
                            formData2.append("padrino", mascotaPut.padrino)
                        }
                        formData2.append("vacuna", mascotaPut.vacuna)
                        formData2.append("categoria", mascotaPut.categoria)

                        axios
                        .put(path2, formData2 )
                        .then(response2 => {
                            formData2 = response2.data;
                            this.$swal.fire(
                                'Mascota asignada exitosamente!',
                                'Presiona ok!',
                                'success'
                            )
                            
                            auxS.persona = personaId
                            auxS.mascotas = []
                            auxS.mascotas.push(this.mascotaId)
                            const path3 = "http://localhost:8000/api/v1.0/adopcion/solicitud/";
                                axios
                                .post(path3, auxS)
                                .then(response3 => {
                                    auxS = response3.data;
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
                        })
                        .catch(error => {
                            this.$swal.fire({
                                icon: 'error',
                                title: 'Oops...',
                                text: error,
                            })
                            console.log(error);
                        });
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
            })
            .catch(error => {
                this.$swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: error,
                })
                console.log(error);
            });
        },
        offNotification() {
            let aux = {}
            for (let i=0; i<this.items.length; i++) {
                if (this.id == this.items[i].id) {
                    aux = this.items[i]
                }
            }
        
        let c = document.createElement('canvas');
        let img = document.getElementById('addImg');
        c.height = img.naturalHeight;
        c.width = img.naturalWidth;
        let ctx = c.getContext('2d');

        ctx.drawImage(img, 0, 0, c.width, c.height);
        let base64String = c.toDataURL('image/jpeg', 0.6);

            delete aux.foto
            delete aux.check 
            let hMascota = null
            let hVacuna = null
            let hTipo = aux.tipo
            if (aux.tipo == 'Padrino') {
                hVacuna = aux.vacuna
                delete aux.vacuna
            } else {
                hMascota = aux.mascota
                delete aux.mascota
            }
            aux = this.objToFormData(aux)
            this.dataURLtoBlob(base64String , function( blob )
                {
                aux.append("foto", blob, 'mascota.jpg');
                });
            aux.append("check", true);
            if (hTipo == 'Padrino') {
                for (let i = 0; i < hVacuna.length; i++) {
                    aux.append('vacuna', hVacuna[i]);
                }
            } else {
                for (let i = 0; i < hMascota.length; i++) {
                    aux.append('mascota', hMascota[i]);
                }
            }
            const path = 'http://localhost:8000/api/v1.0/adopcion/pre-solicitud-administrar/' + this.id + '/';
            axios
                .put(path, aux )
                .then(response => {
                aux = response.data;
                })
                .catch(error => {
                this.$swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: error,
                })
                console.log(error);
                });
        },
    },
    created() {
        this.scrollBehavior(),
        this.getPreSolicitud(),
        this.getMascotas(), 
        this.getVacunas(),
        this.getCategoria()
    },
    beforeUpdate() {
      this.getPersonas(),
      this.getMascotas(),
      this.getVacunas(),
      this.getCategoria()
    },
    beforeDestroy() {
        this.offNotification()
    }
  }
</script>

<style scoped>
    .square {
        width: 100%;
    }
    .square:after {
        content: ‘’;
        display: block;
        padding-bottom: 100%;
    }
    .square .content {
        position: absolute;
        width: 100%;
        height: 100px;
    }
    .square .content img {
        display: block;
        object-fit: cover;
        object-position: center center;
        max-height: 200px;
        width: 100%;
        height: 100%;
    }
</style>