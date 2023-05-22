import QtQuick
import QtQuick.Window
import QtQuick.Controls


ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")


    Rectangle {
        id: root
        color: "transparent"
        anchors {
            fill: parent
            margins: 10
        }

        TextField {
            id: input
            placeholderText: qsTr("Enter some text")
            padding: 10
            focus: true
            anchors {
                left: root.left
                right: root.right
                top: root.top
                margins: 20
            }
            onAccepted: label.text = input.text
        }

        Label { 
            id: label
            // color: system_colors.text
            color: "#FF5722"
            padding: 10
            font.pixelSize: 20
            font.bold: true

            anchors {
                left: root.left
                right: root.right
                top: input.bottom
                margins: 20
            }
            background: Rectangle {
                anchors.fill: parent
                color: Qt.lighter("steelblue",2.0)
                radius: 10  
            }

        }

        Button {
            id: btn_execute
            text: qsTr("Execute")
            anchors {
                bottom: root.bottom
                horizontalCenter: root.horizontalCenter
                margins: 20 
            }
            onClicked: label.text = input.text

        }
    }
}
