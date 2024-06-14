
/*!
    Audiospark Template
    Created on date: 9/24/2023
    Built on date: 10/1/2023
*/


// ## LOADER
window.addEventListener('load', () => {
    setTimeout( () => {
        document.querySelector(".loader-warpper").classList.toggle("loader-warpper-hide");
    }, 2000);
});


// ## NAVBAR MOBILE
function navbarMobileToggle() {
    document.getElementById("navbarMobileToggle").classList.toggle("navbarMobileToggle");
}

// SWITCH MODE
function switchMode() {
    document.body.classList.toggle("switchMode");
    document.getElementById("switchModeBtnDark").classList.toggle("switchModeBtnDarkToggle");
    document.getElementById("switchModeBtnLight").classList.toggle("switchModeBtnLightToggle");

    document.getElementById("logoFooterModeLight").classList.toggle("logoFooterModeLightToggle");
    document.getElementById("logoFooterModeDark").classList.toggle("logoFooterModeDarkToggle");
}

// SEARCH MODE
function searchMode() {
    document.getElementById("searchMode").classList.toggle("searchMode");
    document.getElementById("overlaySearchMode").classList.toggle("overlaySearchMode");
}

// AVATAR DROPDOWN
function avatarDropdown() {
    document.getElementById("avatarDropdown").classList.toggle("avatarDropdown");
}

// SUPPORT & CHAT MODE
function supportChatMode() {
    document.getElementById("supportChatMode").classList.toggle("supportChatMode");
}


// ## BACK TOP
const backTop = document.getElementById("backTop");
const navbarFixed = document.getElementById("navbarFixed");

window.addEventListener("scroll", () => {
    if(window.scrollY > 200) {
        backTop.classList.add("back-top-active");
    } else if(window.scrollY > 50) {
        navbarFixed.classList.add("nav-fixed-active");
    } else {
        backTop.classList.remove("back-top-active");
        navbarFixed.classList.remove("nav-fixed-active");
    }
});


// ## LIKE MUSIC HEADER
function likeMusicHeader() {
    document.getElementById("likeSong").classList.toggle("downloadToggle");
}
function likeMusicPlay() {
    document.getElementById("likeMusicPlay").classList.toggle("likeMusicPlayToggle");
}

// ## PLAY SOUND/MUSIC PLAYER
// Create a global Audio object
var audio1 = new Audio("/static/images/1.mp3");

// Play sound function
// Function to play sound
function playSound(cardId) {
    const audio = document.getElementById(`audio-${cardId}`);
    audio.play().then(() => {
        // Show pause button and hide play button
        document.getElementById(`playBtnPlayCard-${cardId}`).style.display = "none";
        document.getElementById(`pauseBtnPlayCard-${cardId}`).style.display = "inline";
    }).catch(error => {
        console.error('Error playing the audio file:', error);
    });
}

// Function to pause sound
function pauseSound(cardId) {
    const audio = document.getElementById(`audio-${cardId}`);
    audio.pause();
    // Show play button and hide pause button
    document.getElementById(`playBtnPlayCard-${cardId}`).style.display = "inline";
    document.getElementById(`pauseBtnPlayCard-${cardId}`).style.display = "none";
}

// Toggle visibility of play/pause buttons
function togglePlayPauseButtons() {
    const playButton = document.getElementById("playBtnPlayCard");
    const pauseButton = document.getElementById("pauseBtnPlayCard");
    if (audio1.paused) {
        playButton.style.display = "inline";
        pauseButton.style.display = "none";
    } else {
        playButton.style.display = "none";
        pauseButton.style.display = "inline";
    }
}

// Event listener to ensure the correct button is displayed when audio ends
audio1.addEventListener('ended', togglePlayPauseButtons);
function likeMusicPlayer() {
    document.getElementById("likeMusicPlayer").classList.toggle("likeMusicPlayerToggle");
}

// COLLAPSE MUSIC PLAYER
function collapseMusicPlayer() {
    document.getElementById("sectionMusicPlayer").classList.toggle("sectionMusicPlayerToggle");
    document.getElementById("collapseMusicPlayerBtn").classList.toggle("collapseMusicPlayerBtnToggle");
    document.getElementById("expandMusicPlayerBtn").classList.toggle("expandMusicPlayerBtnToggle");
}
function closeSection() {
    document.getElementById("download").classList.toggle("downloadToggle");
}
// FULL PLAYER
function fullPlayer() {
    document.getElementById("fullPlayer").classList.toggle("fullPlayer");
}
function fullPlayerHeaderDropdown() {
    document.getElementById("fullPlayerHeaderDropdown").classList.toggle("fullPlayerHeaderDropdown");
}

// ## DOWNLOAD
function download(beatName) {
    document.getElementById("download").classList.toggle("downloadToggle");

    setTimeout(() => {
        const link = document.createElement('a');
        link.href = `/static/images/${beatName}`;
        link.download = beatName;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }, 3000);
}


// NUMBER ALBUMS
var cardGridLen = document.getElementById("cardGridLen").childElementCount;
var numAlbums = document.getElementById("numAlbums");
numAlbums.innerHTML = cardGridLen;