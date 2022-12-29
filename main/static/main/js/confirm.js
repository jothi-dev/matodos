
window.confirmTodoDelete = function deleteTodo(id) {
    var button = document.querySelector(`#todo-${id}`)

    button.addEventListener('click', function(event) {
        console.log('event', event)
        event.preventDefault()

        if (confirm("Are you you WANT to do this?") == "ok") {
            console.log("Do it!!!")
        }
    })

}
