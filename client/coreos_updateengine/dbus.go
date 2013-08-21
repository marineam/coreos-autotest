package main

import (
	"github.com/guelfey/go.dbus"
	"os"
	"fmt"
	"time"
)

var success = false

func main() {
	conn, err := dbus.SystemBus()
	if err != nil {
	    return	
	}
	msg_chan := make(chan *dbus.Message, 10)
	go handle_func(msg_chan)
	
	call := conn.BusObject().Call("org.freedesktop.DBus.AddMatch", 0,
		"eavesdrop='true',type=signal,interface=org.chromium.UpdateEngineInterface")
	if call.Err != nil {
		fmt.Println("Err")
		os.Exit(1)
	}
	conn.Eavesdrop(msg_chan)
	time.Sleep(20 * time.Second)
	os.Exit(1)
}

func handle_func(msg_chan chan*dbus.Message) {
	<- msg_chan
	os.Exit(0)
}

