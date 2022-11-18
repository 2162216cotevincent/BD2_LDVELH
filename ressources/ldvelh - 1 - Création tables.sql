DROP DATABASE IF EXISTS ldvelh;
CREATE DATABASE ldvelh;

USE ldvelh;


/*CREATION TABLES*/

DROP TABLE IF EXISTS `livre`;
CREATE TABLE `livre` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) NOT NULL,
   PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS `fiche_personnage`;
CREATE TABLE `fiche_personnage` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom_personnage` varchar(255) NOT NULL,
   PRIMARY KEY (`id`)
);


DROP TABLE IF EXISTS `discpipline_kai`;
CREATE TABLE `discipline_kai` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom_discipline` varchar(255) NOT NULL,
   PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS `arme`;
CREATE TABLE `arme` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom_arme` varchar(255) NOT NULL,
   PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS `personnage_discipline`;
CREATE TABLE `personnage_discipline` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_fiche` INT NOT NULL,
  `id_discipline` INT NOT NULL,
   PRIMARY KEY (`id`),
   FOREIGN KEY (id_fiche) REFERENCES fiche_personnage (id),
   FOREIGN KEY (id_discipline) REFERENCES discipline_kai (id)
);

DROP TABLE IF EXISTS `personnage_arme`;
CREATE TABLE `personnage_arme` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_fiche` INT NOT NULL,
  `id_arme` INT NOT NULL,
   PRIMARY KEY (`id`),
   FOREIGN KEY (id_fiche) REFERENCES fiche_personnage (id),
   FOREIGN KEY (id_arme) REFERENCES arme (id)
);



DROP TABLE IF EXISTS `chapitre`;
CREATE TABLE `chapitre` (
  `id` int NOT NULL AUTO_INCREMENT,
  `no_chapitre` INT NOT NULL,
  `texte` TEXT NOT NULL,
  `id_livre` int NOT NULL,
   PRIMARY KEY (`id`),
   FOREIGN KEY (id_livre) REFERENCES livre (id)
);

DROP TABLE IF EXISTS `lien_chapitre`;
CREATE TABLE `lien_chapitre` (
  `id` int NOT NULL AUTO_INCREMENT,
  `no_chapitre_origine` INT NOT NULL,
  `no_chapitre_destination` int NOT NULL,
   PRIMARY KEY (`id`),
   FOREIGN KEY (no_chapitre_origine) REFERENCES chapitre (id),
   FOREIGN KEY (no_chapitre_destination) REFERENCES chapitre (id)
);

DROP TABLE IF EXISTS `sauvegarde`;
CREATE TABLE `sauvegarde` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_fiche` INT NOT NULL,
  `id_chapitre` INT NOT NULL,
   PRIMARY KEY (`id`),
   FOREIGN KEY (id_fiche) REFERENCES fiche_personnage (id),
   FOREIGN KEY (id_chapitre) REFERENCES chapitre (id)
);




/*--INSERTION*/

/*--DISCIPLINE KAI*/
INSERT INTO discipline_kai (nom_discipline) VALUES ("Le camouflage");
INSERT INTO discipline_kai (nom_discipline) VALUES ("La chasse");
INSERT INTO discipline_kai (nom_discipline) VALUES ("Le sixième sens");
INSERT INTO discipline_kai (nom_discipline) VALUES ("L'oriantarion");
INSERT INTO discipline_kai (nom_discipline) VALUES ("La guérison");
INSERT INTO discipline_kai (nom_discipline) VALUES ("La maîtrise des armes");
INSERT INTO discipline_kai (nom_discipline) VALUES ("Bouclier psychique");
INSERT INTO discipline_kai (nom_discipline) VALUES ("Puissance psychique");
INSERT INTO discipline_kai (nom_discipline) VALUES ("Communication animale");
INSERT INTO discipline_kai (nom_discipline) VALUES ("Maître psychique de la matière");

/*--ARMES*/
INSERT INTO arme (nom_arme) VALUES ("Poignard");
INSERT INTO arme (nom_arme) VALUES ("Lance");
INSERT INTO arme (nom_arme) VALUES ("Masse d'armes");
INSERT INTO arme (nom_arme) VALUES ("Sabre");
INSERT INTO arme (nom_arme) VALUES ("Marteau de guerre");
INSERT INTO arme (nom_arme) VALUES ("Épée");
INSERT INTO arme (nom_arme) VALUES ("Hache");
INSERT INTO arme (nom_arme) VALUES ("Épée laser");
INSERT INTO arme (nom_arme) VALUES ("Baton");
INSERT INTO arme (nom_arme) VALUES ("Glaive");
INSERT INTO arme (nom_arme) VALUES ("Arc");

/*--LIVRE*/
INSERT INTO livre (id, nom) VALUES (1, "Les maîtres des ténèbres");









