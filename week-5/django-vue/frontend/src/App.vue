<template>
    <section class="section">
        <div class="container">
            <button
                class="button is-rounded"
                v-if="!authenticated"
                @click="login()">
                Log In
            </button>

            <div class="field is-grouped">
                <p class="control">
                    <button
                        class="button"
                        v-if="authenticated"
                        @click="privateMessage()">
                        Call Private
                    </button>
                </p>
                <p class="control">
                    <button
                        class="button is-rounded"
                        v-if="authenticated"
                        @click="logout()">
                        Log Out
                    </button>
                </p>
            </div>
            {{message}}
            <br />
        </div>
    </section>
</template>

<script>
/* eslint-disable */

import AuthService from './auth/AuthService';
import axios from 'axios';

const API_URL = 'http://localhost:8000';
const AUTH = new AuthService();

export default {
    name: 'app',
    data () {
        this.handleAuthentication();
        this.authenticated = false;
        
        AUTH.authNotifier.on('authChange', authState => {
            this.authenticated = authState.authenticated
        });

        return {
            authenticated: false,
            message: ''
        }
    },
    methods: {
        login () {
            AUTH.login();
        },
        handleAuthentication () {
            AUTH.handleAuthentication();
        },
        logout () {
            AUTH.logout();
        },
        privateMessage () {
            const url = `${API_URL}/api/private`
            return axios.get(url, {headers: { Authorization: `Bearer ${AuthService.getAuthToken()}`}})
                .then(response => {
                    console.log(response.data);
                    this.message = response.data || '';
                });
        }
    }
}
</script>
