<template>
<main>
<div>
    <b-modal
      v-model="show"
      title="Imposta Orario"
      :header-bg-variant="headerBgVariant"
      :header-text-variant="headerTextVariant"
      :body-bg-variant="bodyBgVariant"
      :body-text-variant="bodyTextVariant"
      :footer-bg-variant="footerBgVariant"
      :footer-text-variant="footerTextVariant"
    >
      <b-container fluid>
        <b-row class="mb-1 text-center">
          <b-col cols="3"></b-col>
          <b-col>Orario</b-col>
          <b-col>Materia</b-col>
        </b-row>

        <b-row class="mb-1">
          <b-col cols="3">Seleziona</b-col>
          <b-col>
            <b-form-input
              v-model="oraselezionata"
            disabled></b-form-input>
          </b-col>
          <b-col>
            <b-form-select
              v-model="materiaselezionata"
              :options="listaMaterie"
            ></b-form-select>
          </b-col>
        </b-row>

      </b-container>

      <template v-slot:modal-footer>
        <div class="w-100">
          <p class="float-left">Confermando sovrascriverai l'orario corrente</p>
          <b-button
            variant="primary"
            size="sm"
            class="float-right"
            @click="submitNuovoOrario"
          >
            Conferma
          </b-button>
        </div>
      </template>
    </b-modal>
  </div>  
    <FullCalendar
      class='demo-app-calendar'
      ref="fullCalendar"
      defaultView="timeGridWeek"

      :header="{
        left: '',
        center: 'title',
        right: 'timeGridWeek'
      }"
      :plugins="calendarPlugins"
      :weekends="calendarWeekends"
      :events="calendarEvents"
      :locale="locale"
      :hiddenDays="hiddenDays"
      minTime="08:00:00"
      maxTime="14:00:00"
      aspectRatio=2.335
      firstDay=1
      height=650
      @dateClick="handleDateClick"
      @eventClick="handleEventClick"
      />
</main>
</template>

<script>
    import FullCalendar from '@fullcalendar/vue'
    import dayGridPlugin from '@fullcalendar/daygrid'
    import timeGridPlugin from '@fullcalendar/timegrid'
    import interactionPlugin from '@fullcalendar/interaction'
    import '@fullcalendar/core/locales/it';

    export default {
        props: ["calendarEvents","classeId"],
        components: {
            FullCalendar // make the <FullCalendar> tag available
        },
        data() {
            return {
                calendarPlugins: [ // plugins must be defined in the JS
                    dayGridPlugin,
                    timeGridPlugin,
                    interactionPlugin // needed for dateClick
                ],
                
                //defaultView: 'timeGridDay',//timeGridDay agendaWeek
                calendarWeekends: true,
                hiddenDays: [0],
                calendarEvents: this.calendarEvents,
                locale:'it',



                //MODAL CONFIG
                show: false,
                eventSelected: 0,
                oraselezionata: 8,
                giornoselezionato: 0,
                materiaselezionata: null,
                listaMaterie:[
                                { value: 1, text: 'Diritto ed economia' },
                                { value: 2, text: 'Discipline sportive' },
                                { value: 3, text: 'Storia dell\'arte'}, 
                                { value: 4, text: 'Filosofia'},
                                { value: 5, text: 'Fisica'},
                                { value: 6, text: 'Informatica'},
                                { value: 7, text: 'Religione'},
                                { value: 8, text: 'Latino'},
                                { value: 9, text: 'Inglese'},
                                { value: 10, text: 'Letteratura'},
                                { value: 11, text: 'Matematica'},
                                { value: 12, text: 'Scienze'},
                                { value: 14, text: 'Storia e Geografia'},
                                { value: 15, text: 'Nessuna'},
                              ],
                headerBgVariant: 'dark',
                headerTextVariant: 'light',
                bodyBgVariant: 'light',
                bodyTextVariant: 'dark',
                footerBgVariant: 'warning',
                footerTextVariant: 'dark'
 
            }
        },
        mounted(){              
              let calendarApi = this.$refs.fullCalendar.getApi();
              calendarApi.render();
            },
          methods: {
                handleDateClick(arg) {
                  this.oraselezionata = arg.date.getHours()
                  this.giornoselezionato = arg.date.getDay()
                  //this.materiaselezionata = arg.date.getDay()
                  console.log(this.oraselezionata)
                  console.log(this.giornoselezionato)
                  this.eventSelected= 0
                  this.show=true

                  
                },
                handleEventClick(arg) {
                  this.oraselezionata = arg.event.start.getHours()
                  this.giornoselezionato = arg.event.start.getDay()

                  this.eventSelected = arg.event.groupId
                  console.log(this.oraselezionata)
                  console.log(this.giornoselezionato)

                  this.show=true
                    /*
                    if (confirm('Would you like to add an event to ' + arg.dateStr + ' ?')) {
                        this.calendarEvents.push({ // add new event data
                        title: 'New Event',
                        start: arg.date,
                        allDay: arg.allDay
                        })
                    }*/
                },
                async submitNuovoOrario(){
                  if (this.eventSelected != 0){
                     const config = {
                        headers: { "content-type": "multipart/form-data" }
                      };
                      let formData = new FormData();
                      //formData.append('numero_ora',this.oraselezionata)
                      //formData.append('giorno_della_settimana',this.giornoselezionato)
                      formData.append('materia',this.materiaselezionata)
                      try {
                        //let response = await this.$axios.$post("api/classe/oramateria/", formData, config);
                        let response = await this.$axios.$put(`api/classe/oramateria/${this.eventSelected}/`, formData, config);
                        console.log(response)
                        location.reload()
                      } catch (e) {
                        console.log(e);
                      }
                  }else{
                      const config = {
                        headers: { "content-type": "multipart/form-data" }
                      };
                      let formData = new FormData();
                      //for (let data in this.classe) {
                      //  formData.append(data, this.classe[data]);
                      //}
                      formData.append('numero_ora',this.oraselezionata)
                      formData.append('giorno_della_settimana',this.giornoselezionato)
                      console.log(this.materiaselezionata)
                      formData.append('materia',this.materiaselezionata)
                      formData.append('classe',this.classeId)
                      try {
                        let response = await this.$axios.$post("api/classe/oramateria/", formData, config);
                        console.log(response)
                        location.reload()
                      } catch (e) {
                        console.log(e);
                      }
                  }
                },

            }
    }
</script>

<style lang='scss'>
// you must include each plugins' css
// paths prefixed with ~ signify node_modules
@import '@fullcalendar/core/main.css';
@import '@fullcalendar/daygrid/main.css';
@import '@fullcalendar/timegrid/main.css';

</style>
<!--
<style>

  #calendar-container {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
  }

  .demo-topbar { /* will be stripped out */
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 40px;
  }

  .demo-topbar + #calendar-container { /* will be stripped out */
    top: 40px;
  }

  .fc-header-toolbar {
    /*
    the calendar will be butting up against the edges,
    but let's scoot in the header's buttons
    */
    padding-top: 1em;
    padding-left: 1em;
    padding-right: 1em;
  }

</style>
-->