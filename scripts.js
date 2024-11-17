// Команды, разделённые на категории
const commands = {
    miniGames: [
        { command: "дрочнуть", description: "Мини-игра: +1 счёт, шанс получить дрочкоин.", rank: 0 },
        { command: "/top_droch", description: "Показывает топ 10 дрочеров.", rank: 0 },
        { command: "/use", description: "Использовать предмет.", rank: 0 },
        { command: "/case", description: "Открыть кейс раз в 3 часа.", rank: 0 },
        { command: "/inventory", description: "Показать ваши предметы.", rank: 0 },
        { command: "/items", description: "Отправляет описание предметов в ЛС.", rank: 0 },
        { command: "/shop", description: "Показывает доступные предметы и их стоимость.", rank: 0 },
        { command: "/buy", description: "Купить предмет за дрочкоины.", rank: 0 },
    ],
    filmCommands: [
        { command: "/film", description: "Начать игру 'Угадай фильм'.", rank: 0 },
        { command: "/skip", description: "Пропустить текущий фильм.", rank: 1 },
        { command: "/top", description: "Показать топ игроков.", rank: 0 },
    ],
    pranks: [
        { command: "тролл", description: "Отправить тролл-картинку.", rank: 1 },
        { command: "выебать", description: "Уникальная команда для ответа на сообщение.", rank: 1 },
    ],
    muteCommands: [
        { command: "rek", description: "Мут на 5 дней.", rank: 2 },
        { command: "rod", description: "Мут на 1 день.", rank: 2 },
        { command: "18p", description: "Мут на 5 часов.", rank: 2 },
        { command: "prik", description: "Мут на 1 минуту.", rank: 1 },
        { command: "unm", description: "Снимает мут с пользователя.", rank: 1 },
    ],
    adminCommands: [
        { command: "/add", description: "Добавляет нового пользователя с рангом.", rank: 3 },
        { command: "/remove", description: "Удаляет пользователя.", rank: 3 },
        { command: "/show", description: "Показывает всех пользователей и их ранги.", rank: 1 },
        { command: "/add_items", description: "Добавляет предмет пользователю.", rank: 3 },
        { command: "/cd_case", description: "Сбрасывает КД кейса пользователю.", rank: 3 },
    ],
};

// Генерация списка команд
function renderCommands() {
    const sections = {
        miniGames: document.getElementById("mini-games-section"),
        filmCommands: document.getElementById("film-commands-section"),
        pranks: document.getElementById("pranks-section"),
        muteCommands: document.getElementById("mute-commands-section"),
        adminCommands: document.getElementById("admin-commands-section"),
    };

    Object.entries(commands).forEach(([category, cmds]) => {
        cmds.forEach((cmd) => {
            const commandItem = document.createElement("div");
            commandItem.classList.add("command");

            const commandName = document.createElement("h2");
            commandName.textContent = cmd.command;

            const commandDescription = document.createElement("p");
            commandDescription.textContent = cmd.description;

            const commandRank = document.createElement("p");
            commandRank.textContent = `Требуемый ранг: ${cmd.rank}`;

            commandItem.appendChild(commandName);
            commandItem.appendChild(commandDescription);
            commandItem.appendChild(commandRank);

            sections[category].appendChild(commandItem);
        });
    });
}

// Запуск функции при загрузке страницы
document.addEventListener("DOMContentLoaded", renderCommands);
// Скрипт для кнопки "Наверх"
document.addEventListener("DOMContentLoaded", function () {
    const scrollToTopBtn = document.getElementById("scrollToTopBtn");

    // Показать кнопку при прокрутке вниз
    window.addEventListener("scroll", function () {
        if (window.scrollY > 300) {
            scrollToTopBtn.classList.add("show");
        } else {
            scrollToTopBtn.classList.remove("show");
        }
    });

    // Прокрутка вверх при клике
    scrollToTopBtn.addEventListener("click", function () {
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    });
});