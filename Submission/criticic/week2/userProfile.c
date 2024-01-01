#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct UserProfile {
    char username[8];
    char bio[64];
    int isAdmin;
};

void displayProfile(struct UserProfile *profile) {
    printf("Username: %s\n", profile->username);
    printf("Bio: %s\n", profile->bio);
    printf("Is Admin: %s\n", profile->isAdmin ? "Yes" : "No");
}

int main() {
    struct UserProfile *currentUser = (struct UserProfile *)malloc(sizeof(struct UserProfile));
    currentUser->isAdmin = 0;

    printf("Enter your username: ");
    scanf("%s", currentUser->username);

    printf("Enter your bio: ");
    scanf("%s", currentUser->bio);

    displayProfile(currentUser);

    if (currentUser->isAdmin == 1) {
        printf("Welcome, admin!\n");
        printf("Hello Admin, I have secretly collected the data of 7639320 users\n");
        printf("functions redacted\n");
    } else {
        printf("Access level: User\n");
        printf("Hello User, I am HaxGPT, your friendly neigbourhood AI.\n");
        printf("functions redacted\n");
    }

    free(currentUser);
    return 0;
}