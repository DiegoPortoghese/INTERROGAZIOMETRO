<template>
<div class="messaging">
  <div class="inbox_msg">
	<div class="inbox_people">
	  <div class="headind_srch">
		<div class="recent_heading">
		  <h4>Lista conversazioni</h4>
		</div>
	  </div>
	  <div class="inbox_chat scroll">
        
		<div v-for="chatblock in different_peoplechat" class="chat_list" v-on:click="selectChat(chatblock.user)" v-bind:class="{'active_chat': chatblock.user == selectedChatUser}"> <!-- active_chat -->
		  <div class="chat_people" >
			<div class="chat_ib">
			  <h5>{{ chatblock.fullname }} <span class="chat_date"> {{chatblock.date.substring(5, 10) }}</span></h5>
			  <p>{{ chatblock.msg }}</p>
			</div>
		  </div>
		</div>

	  </div>
	</div>
	<div class="mesgs">
	  <div class="msg_history" id="msg_history_scrolling">
        
		<div v-for="message in selectedChatmessages" v-bind:class="{'incoming_msg': !message.isMyMessage , 'outgoing_msg': message.isMyMessage}" >
		  <div v-bind:class="{'received_msg': !message.isMyMessage , 'sent_msg': message.isMyMessage}">
			<div class="received_withd_msg">
			  <p><b>{{ message.isMyMessage ?  'Tu' : message.fullname}}</b><br>{{message.msg}}</p>
			  <span class="time_date"> {{message.date.substring(11, 16) }} | {{message.date.substring(5, 10) }}</span></div>
		  </div>
		</div>
		
		
	  </div> 
	  <div class="type_msg">
		<div class="input_msg_write" >
		  <input type="text" class="write_msg" placeholder=" Type a message" v-model="sendMessage.message" v-on:keyup.enter="SendMessage" />
		  <button class="msg_send_btn" type="submit"><i class="fa fa-paper-plane" aria-hidden="true" v-on:click="SendMessage"></i></button>
		</div>
	  </div>
	</div>
  </div>
</div>
 
</template>

<style scoped>
/*---------chat window---------------*/
.container{
    max-width:900px;
}
.inbox_people {
	background: #fff;
	float: left;
	overflow: hidden;
	width: 30%;
	border-right: 1px solid #ddd;
}

.inbox_msg {
	border: 0px solid #ddd;
	clear: both;
	overflow: hidden;
}

.top_spac {
	margin: 20px 0 0;
}

.recent_heading {
	float: left;
	width: 40%;
}

.srch_bar {
	display: inline-block;
	text-align: right;
	width: 60%;
}

.headind_srch {
	padding: 10px 29px 10px 20px;
	overflow: hidden;
	border-bottom: 1px solid #c4c4c4;
}

.recent_heading h4 {
	color: #0465ac;
    font-size: 16px;
    margin: auto;
    line-height: 29px;
}

.srch_bar input {
	outline: none;
	border: 1px solid #cdcdcd;
	border-width: 0 0 1px 0;
	width: 80%;
	padding: 2px 0 4px 6px;
	background: none;
}

.srch_bar .input-group-addon button {
	background: rgba(0, 0, 0, 0) none repeat scroll 0 0;
	border: medium none;
	padding: 0;
	color: #707070;
	font-size: 18px;
}

.srch_bar .input-group-addon {
	margin: 0 0 0 -27px;
}

.chat_ib h5 {
	font-size: 15px;
	color: #464646;
	margin: 0 0 8px 0;
}

.chat_ib h5 span {
	font-size: 13px;
	float: right;
}

.chat_ib p {
    font-size: 12px;
    color: #989898;
    margin: auto;
    display: inline-block;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.chat_img {
	float: left;
	width: 11%;
}

.chat_img img {
	width: 100%
}

.chat_ib {
	float: left;
	padding: 0 0 0 15px;
	width: 88%;
}

.chat_people {
	overflow: hidden;
	clear: both;
}

.chat_list {
	border-bottom: 1px solid #ddd;
	margin: 0;
	padding: 18px 16px 10px;
}

.inbox_chat {
	height: 82vh;
	overflow-y: scroll;
}

.active_chat {
	background: #e8f6ff;
}

.incoming_msg_img {
	display: inline-block;
	width: 6%;
}

.incoming_msg_img img {
	width: 100%;
}

.received_msg {
	display: inline-block;
	padding: 0 0 0 10px;
	vertical-align: top;
	width: 92%;
}

.received_withd_msg p {
	background: #ebebeb none repeat scroll 0 0;
	border-radius: 0 15px 15px 15px;
	color: #646464;
	font-size: 14px;
	margin: 0;
	padding: 5px 10px 5px 12px;
	width: 100%;
}

.time_date {
	color: #747474;
	display: block;
	font-size: 12px;
	margin: 8px 0 0;
}

.received_withd_msg {
	width: 57%;
}

.mesgs{
	float: left;
	padding: 00px 0px 0 25px;
	width:70%;
}

.sent_msg p {
	background:#0465ac;
	border-radius: 12px 15px 15px 0;
	font-size: 14px;
	margin: 0;
	color: #fff;
	padding: 5px 10px 5px 12px;
	width: 100%;
}

.outgoing_msg {
	overflow: hidden;
	margin: 26px 0 26px;
}

.sent_msg {
	float: right;
	width: 46%;
}

.input_msg_write input {
	background: rgba(0, 0, 0, 0) none repeat scroll 0 0;
	border: medium none;
	color: #4c4c4c;
	font-size: 15px;
	min-height: 48px;
	width: 100%;
	outline:none;
}

.type_msg {
	border-top: 1px solid #c4c4c4;
	position: absolute;
    bottom:0;
    right:0;
    left:30%;
}

.msg_send_btn {
	background: #05728f none repeat scroll 0 0;
	border:none;
	border-radius: 50%;
	color: #fff;
	cursor: pointer;
	font-size: 15px;
	height: 33px;
	position: absolute;
	right: 0;
	top: 11px;
	width: 33px;
}

.messaging {
	padding: 0 0 0 0;
}

.msg_history {
    padding-top:20px;
	height: 85vh;
	overflow-y: auto;
}
</style>

<script>
import { mapGetters } from 'vuex'

export default {
    layout: 'no-footer',
    data(){
        return {
            chatmessages: [],
            selectedChatmessages: [],
            different_peoplechat: [
                {user:0,fullname:'',msg:'',date:''}
            ],
            selectedChatUser: 0,
            sendMessage: {
                from_user: 0,
                to_user: 0,
                displayed: false,
                message: ''
            },
            timer: ''
        };
    },
    computed: {
        ...mapGetters(['isAuthenticated', 'loggedInUser'])
    },
    created () {
        this.timer = setInterval(this.intervalRefresh, 5000)
    },
    mounted() {
		this.asyncData() 
    },
    updated: function () {
        this.$nextTick(function () {
            var objDiv = document.getElementById("msg_history_scrolling");
            objDiv.scrollTop = objDiv.scrollHeight;
        })
    },
    beforeDestroy () {
      clearInterval(this.timer)
    },
    methods:{
        async asyncData() {
            var self = this;
                try {
                    await self.$axios.$get("api/chatmessages/").then(function(data){
                        self.chatmessages = data;
                    });
                    let currentuserid = this.loggedInUser.profile[0].fields.user
                    var array_diff_message_buffer = []
                    var array_diff_user_buffer = []
                    for (let key in self.chatmessages){
                        var message_buff = self.chatmessages[key]
                        if (message_buff.from_user != currentuserid){
                            if (!array_diff_user_buffer.includes(message_buff.from_user)){
                                array_diff_user_buffer.push(message_buff.from_user)
                                array_diff_message_buffer.push({user: message_buff.from_user,fullname: message_buff.from_user_first_name +' '+ message_buff.from_user_last_name , msg: message_buff.message,date: message_buff.creation_date})
                            }
                        }
                        if (message_buff.to_user != currentuserid){
                            if (!array_diff_user_buffer.includes(message_buff.to_user)){
                                array_diff_user_buffer.push(message_buff.to_user)
                                array_diff_message_buffer.push({user: message_buff.to_user,fullname: message_buff.to_user_first_name +' '+ message_buff.to_user_last_name , msg: message_buff.message,date: message_buff.creation_date})
                            }
                        }
                    }
                    this.different_peoplechat = array_diff_message_buffer;
                    if (this.different_peoplechat[0].user != 0){
                        this.selectedChatUser = this.different_peoplechat[0].user
                        this.selectChat(this.selectedChatUser)
                    }
                    console.log(this.different_peoplechat)
                }
                catch (error) {
                    // TODO: migliorare la segnalazione errori
                    console.log(error)
                }
            },
        async selectChat(user){
            var self = this;
            try {
                await self.$axios.$get("api/chatmessages/").then(function(data){
                    self.chatmessages = data;
                });
                let currentuserid = this.loggedInUser.profile[0].fields.user
                var array_diff_message_buffer = []
                var array_diff_user_buffer = []
                for (let key in self.chatmessages){
                    var message_buff = self.chatmessages[key]
                    if (message_buff.from_user != currentuserid){
                        if (!array_diff_user_buffer.includes(message_buff.from_user)){
                            array_diff_user_buffer.push(message_buff.from_user)
                            array_diff_message_buffer.push({user: message_buff.from_user,id: message_buff.id,displayed: message_buff.displayed,fullname: message_buff.from_user_first_name +' '+ message_buff.from_user_last_name , msg: message_buff.message,date: message_buff.creation_date})
                        }
                    }
                    if (message_buff.to_user != currentuserid){
                        if (!array_diff_user_buffer.includes(message_buff.to_user)){
                            array_diff_user_buffer.push(message_buff.to_user)
                            array_diff_message_buffer.push({user: message_buff.to_user,id: message_buff.id,displayed: message_buff.displayed,fullname: message_buff.to_user_first_name +' '+ message_buff.to_user_last_name , msg: message_buff.message,date: message_buff.creation_date})
                        }
                    }
                }
                this.different_peoplechat = array_diff_message_buffer;
                console.log(this.different_peoplechat)
            }
            catch (error) {
                // TODO: migliorare la segnalazione errori
                console.log(error)
            }
            this.$forceUpdate();
            var self = this;
            this.selectedChatUser = user
            try{
                let buff_selectedChatmessages = []
                let currentuserid = this.loggedInUser.profile[0].fields.user
                for (let key in self.chatmessages){
                    var message_buff = self.chatmessages[key]
                    if (message_buff.from_user == user || message_buff.to_user == user){
                        if (message_buff.from_user != currentuserid){
                            buff_selectedChatmessages.push({isMyMessage: false,id: message_buff.id,displayed: message_buff.displayed,user: message_buff.from_user,fullname: message_buff.from_user_first_name +' '+ message_buff.from_user_last_name , msg: message_buff.message,date: message_buff.creation_date})
                        }
                        if (message_buff.to_user != currentuserid){
                            buff_selectedChatmessages.push({isMyMessage: true,id: message_buff.id,displayed: message_buff.displayed,user: message_buff.to_user,fullname: message_buff.to_user_first_name +' '+ message_buff.to_user_last_name , msg: message_buff.message,date: message_buff.creation_date})
                        }
                    }
                }
                this.selectedChatmessages = buff_selectedChatmessages.reverse()
                console.log(this.selectedChatmessages)
            }catch(error){
                console.log(error)
            }
            try{
                const config = {
                        headers: { "content-type": "application/json" }
                    };
                for(let key in this.chatmessages){
                    if(this.chatmessages[key].displayed == false && this.chatmessages[key].from_user != this.loggedInUser.profile[0].fields.user){
                        let jsData = {
                            displayed: true,
                        }
                        let response = await this.$axios.$put(`api/chatmessages/${this.chatmessages[key].id}/`, jsData, config);
                    }
                }
                }catch(error){
                    console.log(error)
			}
        },
        async SendMessage(){
            if (this.sendMessage.message != ''){
                const config = {
                    headers: { "content-type": "multipart/form-data" }
                };
                try {
                    console.log(this.sendMessage)
                    let formData = new FormData();
                        formData.append('from_user',this.loggedInUser.profile[0].fields.user)
                        formData.append('to_user',this.selectedChatUser)
                        formData.append('message',this.sendMessage.message)

                    let response =  this.$axios.$post(`api/chatmessages/`, formData, config);
                    this.sendMessage.message = ''                    
                    await this.selectChat(this.selectedChatUser)
                } catch (e) {
                    console.log(e);
                }
            }
		},
		async SetDisplayed(){
            try{
                const config = {
                        headers: { "content-type": "application/json" }
                    };
                for(let key in this.chatmessages){
                    if(this.chatmessages[key].displayed == false && this.chatmessages[key].from_user != this.loggedInUser.profile[0].fields.user){
                        let jsData = {
                            displayed: true,
                        }
                        let response = await this.$axios.$put(`api/chatmessages/${this.chatmessages[key].id}/`, jsData, config);
                    }
                }
                }catch(error){
                    console.log(error)
			}
			
        },
        intervalRefresh(){
            if (this.selectedChatUser != 0){
            this.selectChat(this.selectedChatUser);
                this.SetDisplayed()
            }else{
                this.asyncData()
                this.SetDisplayed()
            }
        },
        cancelAutoUpdate () { clearInterval(this.timer) }
    },
    
}
</script>
