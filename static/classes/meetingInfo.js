class MeetingInfo {
    constructor(info) {
        this.errors = info["errors"];
        this.question = info["questions"];
        this.moods = info["moods"];
        this.textResponses = info["responses"]["text"];
        this.emojiResponses = info["responses"]["emoji"];
        this.multChoiceResponses = info["responses"]["mult_choice"];
    }
}