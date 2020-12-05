const chat_box = Vue.component('chat_box', {
    delimiters: ['[[', ']]'],
    props: ['user_pk', 'is_coach'],
    data: function () {
        return {
            chat_data: []
        }
    },
    async created() {
        await this.get_chat_data(); 
    },
    methods: {
        async get_chat_data() {
            if (this.user_pk != ''){
                var response = await fetch('http://localhost:8000/api/chat/' + String(this.user_pk) + '/');
                this.chat_data = await response.json();
            }
        },
        async send_message() {
            alert("SAdasd");
            var url = 'http://localhost:8000/api/chat/';
            var msg = String(document.getElementById("input_message").value).replace(/(\r\n|\n|\r)/gm, "")
            console.log(msg);
            await fetch(url, {
                method: 'post',
                headers: {
                'X-CSRFTOKEN' : get_cookie('csrftoken'),
                'Content-Type': 'application/json'
                },
                body:JSON.stringify({
                    "pk": parseInt(this.user_pk),
                    "message" : msg
                })
            });
            document.getElementById("input_message").value = ""
            await this.get_chats(parseInt(this.user_pk));
        },
    },
    template: `<div id="selected_chat" class="container floating_chat" >
                    <div class="row">
                        <div class="card" style="width:100%;float:right;">
                            <div class="card-header">Chat</div>
                            <ul class="chat-list" style="width=300px;height:500px;overflow:scroll;">
                                <div v-for="chat in chat_data" :key="chat.pk">
                                    <li v-if='user_pk == chat.sender.pk' class="in">
                                        <div class="chat-img">
                                            <img alt="Avatar" :src="[[ chat.sender.profile_photo ]]">
                                        </div>
                                        <div class="chat-body">
                                            <div class="chat-message">
                                                <h5>[[ chat.sender.first_name ]] [[ chat.sender.last_name ]]</h5>
                                                <p>[[ chat.message ]]</p>
                                            </div>
                                        </div>
                                    </li>
                                    <li v-else class="out">
                                        <div class="chat-img">
                                            <img alt="Avatar" :src="[[ chat.sender.profile_photo ]]">
                                        </div>
                                        <div class="chat-body">
                                            <div class="chat-message">
                                                <h5>[[ chat.sender.first_name ]] [[ chat.sender.last_name ]]</h5>
                                                <p>[[ chat.message ]]</p>
                                            </div>
                                        </div> 
                                    </li> 
                                </div> 
                            </ul>
                            <div class="form-group mt-3 mb-0">
                                <textarea v-on:keyup.enter="send_message()" class="form-control" id="input_message" rows="1"  placeholder="Type your message here..."></textarea>
                            </div>
                        </div>
                    </div>
                </div>
    `,
    watch: { 
        user_pk: function(new_user_pk, old_user_pk) { // watch it
            this.get_chat_data(); 
      }
    }
})
