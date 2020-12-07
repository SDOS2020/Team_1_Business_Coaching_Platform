const connectionList = Vue.component('connection-list', {
    delimiters: ['[[', ']]'],
    props: ['is_coach'],
    data: function () {
        return {
            my_connections: []
        }
    },
    async created() {
        await this.get_connections(); 
    },
    methods: {
        async get_connections() {
            var response = await fetch('http://localhost:8000/api/connection/');
            this.my_connections = await response.json();
        },
    },
    template: `<div id="connection_list">
                    <ul class="users" style="height: 300px; float: left; width: 200px;">
                        <div v-if='is_coach == "True"'>
                            <li v-for="connection in my_connections" v-if="connection.accepted" :key="connection.pk" class="person" v-on:click="$emit('request_chat',connection.coachee)">
                                <div class="user">
                                    <img :src="connection.coachee.profile_photo" alt="Profile_photo">
                                </div>
                                <p class="name-time">
                                    <span class="name"> [[ connection.coachee.first_name ]] [[ connection.coachee.last_name ]]</span>
                                </p>
                            </li>
                        </div> 
                        <div v-else>
                            <li v-for="connection in my_connections" v-if="connection.accepted" :key="connection.pk" class="person" v-on:click="$emit('request_chat',connection.coach)">
                                <div class="user">
                                    <img :src="connection.coach.profile_photo" alt="Profile_photo">
                                </div>
                                <p class="name-time">
                                    <span class="name"> [[ connection.coach.first_name ]] [[ connection.coach.last_name ]]</span>
                                </p>
                            </li>
                        </div>       
                    </ul>
                </div>
    `
})